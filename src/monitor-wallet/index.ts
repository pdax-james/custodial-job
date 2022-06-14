import config from 'config'

const DATADOG_KEY = config.get('datadog.key')

export default async () => {
  console.log('check wallets')
  console.log('logging to', DATADOG_KEY)
}
