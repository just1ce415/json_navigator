# json_navigator
(Laboratory 3.2)
json_navigator is a module to navigate through json file.

## Example usage

### 1) Step
State the path of the .json file you want to navigate in json_navigator.py:
```python
PATH = 'path' # STATE YOUR PATH HERE
```


### 2) Run the program
```bash
$ python json_navigator.py
['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
tests/friends_list_Obama.json:/ $ users    # PICKING THE 'USERS VARIANT'
range(0, 10)
tests/friends_list_Obama.json:/users/ $ 6   # YOU SHOULD STATE THE PROPER RANGE
['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'proe', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type']
tests/friends_list_Obama.json:/users/[6]/ $ status   # THE WHOLE PATH WILL BE DISPLYED BEFORE $
['text', 'in_reply_to_screen_name', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'quoted_status_id', 'quoted_status_id_str', 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'possibly_sensitive', 'lang']
tests/friends_list_Obama.json:/users/[6]/status/ $ text
'@RahulRajkumar11 is being modest.  The #ValuePlatform from major providers in NC will bring higher quality, more af… https://t.co/nJWYVtHgBC'
```
