import monitorWallet from './monitor-wallet'

const INTERVAL_MONITOR_WALLET = 60000 // 1 minute

setInterval(monitorWallet, INTERVAL_MONITOR_WALLET)