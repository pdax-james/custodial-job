import boto3
import os

def get_parameter(key, decrypt=False):
    client = boto3.client('ssm', region_name='ap-southeast-1')
    resp = client.get_parameter(Name=key, WithDecryption=decrypt)
    return resp

def write_application_config(fp):
    prefix = '{}_{}_{}'.format(
        os.environ['PROJECT'],
        os.environ['ENVIRONMENT'],
        os.environ['SERVICE']
    )

    key = '{}_datadog_key'.format(prefix)
    param = get_parameter(key, True)
    datadog_key = param['Parameter']['Value']

    with open("templates/application.tmpl", "r") as tmpl:
        template = tmpl.read()
        conf = template.format(
            datadog_key=datadog_key,
        )
        fp.write(conf)

def main():
    target_file = '../config/{}.js'.format(
        os.environ['ENVIRONMENT']
    )
    with open(target_file, 'w') as fp:
        fp.write("module.exports = {\n")
        write_application_config(fp)
        fp.write("}\n")

if __name__ == "__main__":
    main()
