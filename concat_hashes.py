with open('./Hashes', 'r') as h:
    non_paths = h.read().strip().split('\n')
with open('./Hashes_FullPath', 'r') as h:
    paths = h.read().strip().split('\n')

all_hashes = non_paths + paths
with open('./Hashes_all', 'w') as f:
    f.write('\n'.join(all_hashes))
