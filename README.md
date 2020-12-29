# key-value

1. It can be initialized using an optional file path. If one is not provided.
2. Key string capped at 32 characters and Value must be a JSON object capped at 16KB.
3. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
4. Only one process can access the datastore (local file) at a time.
5. The data stored is Thread safe.

# Usage
- You can use command __crd__ to start the python file
- It creates a key-value.json file if its not present.
- If the json file is present it will use that.

# Name   |  Commands

    - Create - create key value (or) create key value time_to_live[integer]
    - Read   - read key
    - Delete - delete key
    - Modify - modify key data
    - Exit   - exit
    - Show   - show
