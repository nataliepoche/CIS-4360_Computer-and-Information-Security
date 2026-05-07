all: crack_hashes

crack_hashes:
	echo '#!/usr/bin/env python3' > crack_hashes
	cat custom_hash.py >> crack_hashes
	chmod +x crack_hashes

clean:
	rm -f crack_hashes