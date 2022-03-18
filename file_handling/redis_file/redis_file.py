data = {'acllog-max-len': '128',
 'activerehashing': 'yes',
 'always-show-logo': 'no',
 'aof-load-truncated': 'yes',
 'aof-rewrite-incremental-fsync':'yes', 
 'aof-use-rdb-preamble': 'yes', 
 'appendfilename': '"appendonly.aof"', 
 'appendfsync': 'everysec', 
 'appendonly': 'no',
 'auto-aof-rewrite-min-size': 
 '64mb', 'auto-aof-rewrite-percentage': '100', 'bind': '0.0.0.0', 'client-output-buffer-limit': 'pubsub 32mb 8mb 60', 'cluster-enabled': 'yes', 'daemonize': 'no', 'databases': '16', 'dbfilename': 'dump.rdb', 'dir': '/var/lib/redis/6379', 'disable-thp': 'yes', 'dynamic-hz': 'yes', 'hash-max-ziplist-entries': '512', 'hash-max-ziplist-value': '64', 'hll-sparse-max-bytes': '3000', 'hz': '10', 'jemalloc-bg-thread': 'yes', 'latency-monitor-threshold': '0', 'lazyfree-lazy-eviction': 'no', 'lazyfree-lazy-expire': 'no', 'lazyfree-lazy-server-del': 'no', 'lazyfree-lazy-user-del': 'no', 'lazyfree-lazy-user-flush': 'no', 'list-compress-depth': '0', 'list-max-ziplist-size': '-2', 'logfile': '/var/log/redis_6379.log', 'loglevel': 'notice', 'lua-time-limit': '5000', 'masterauth': '1234 ', 'no-appendfsync-on-rewrite': 'no', 'notify-keyspace-events': '""', 'oom-score-adj': 'no', 'oom-score-adj-values': '0 200 800', 'pidfile': '/var/run/redis_6379.pid', 'port': '6379', 'proc-title-template': '"{title} {listen-addr} {server-mode}"', 'protected-mode': 'yes', 'rdb-del-sync-files': 'no', 'rdb-save-incremental-fsync': 'yes', 'rdbchecksum': 'yes', 'rdbcompression': 'yes', 'repl-disable-tcp-nodelay': 'no', 'repl-diskless-load': 'disabled', 'repl-diskless-sync': 'no', 'repl-diskless-sync-delay': '5', 'replica-lazy-flush': 'no', 'replica-priority': '100', 'replica-read-only': 'yes', 'replica-serve-stale-data': 'yes', 'requirepass': '1234', 'save': '""', 'set-max-intset-entries': '512', 'set-proc-title': 'yes', 'slowlog-log-slower-than': '10000', 'slowlog-max-len': '128', 'stop-writes-on-bgsave-error': 'yes', 'stream-node-max-bytes': '4096', 'stream-node-max-entries': '100', 'supervised': 'systemd', 'tcp-backlog': '511', 'tcp-keepalive': '300', 'timeout': '0', 'zset-max-ziplist-entries': '128', 'zset-max-ziplist-value': '64'}

with open("redis2.conf","w") as file:
    for k,v in data.items():
        line= " ".join((k,v)) + "\n"
        file.write(line)