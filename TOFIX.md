# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/filesystem_find_dupes.py:41` - the menu prints `{i}) keep {f}` but the chosen index is then passed to `os.unlink(v[p])` at line 48, so the file the user asked to keep is the one deleted; delete every entry except `v[p]` (or relabel the menu as "delete").

## Medium

- `src/filesystem_find_dupes.py:34` - `hashmap[h]=[ exist_hash[h], fullname ]` replaces the list on each new duplicate, so with three or more identical files only the first and the latest are offered and the rest are silently lost; append to the list instead (e.g. `hashmap.setdefault(h, [exist_hash[h]]).append(fullname)`).
- `pyproject.toml:10` - depends on `oauth2client`, which Google deprecated in 2017 and no longer maintains; `src/list_files.py:11-12` and `src/setup_credentials.py:10-12` use it for the whole auth flow. Port to `google-auth` + `google-auth-oauthlib` (`InstalledAppFlow`, `Credentials.from_authorized_user_file`).

## Low

- `src/list_files.py:16` - `SCOPES` is assigned twice (lines 16-17), and `SCOPES`, `CLIENT_SECRET_FILE` and `APPLICATION_NAME` (lines 16-20) are never used in this script (scopes are fixed by `setup_credentials.py`); delete them.
- `src/list_files.py:14` - the comment says to delete `~/.credentials/drive-python-quickstart.json` when changing scopes, but the code stores credentials in `~/.credentials/myworld.json` (line 24); same stale comment at `src/setup_credentials.py:14-15`. Fix the path in both comments.
- `src/filesystem_find_dupes.py:19` - reads files in 128-byte chunks, which makes hashing large trees very slow; use a larger buffer (e.g. 64 KiB) or `hashlib.file_digest`.
- `doc/links.txt:2` - the Drive quickstart URL `developers.google.com/drive/v3/web/quickstart/python` is the old path; update to `https://developers.google.com/drive/api/quickstart/python`.
