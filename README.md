# ZiProto

ZiProto is used to serialize data, ZiProto is designed with the intention to be
used for transferring data instead of using something like JSON which can use
up more bandwidth when you don't intend to have the data shown to the public
or end-user

## Setup
```bash
python setup.py install
```

## Usage

To encode data, this can be done simply
```python
>> import ziproto
>> ziproto.encode({"foo": "bar", "fruits": ['apple', 'banana']})
bytearray(b'\x82\xa6fruits\x92\xa5apple\xa6banana\xa3foo\xa3bar')
```

The same can be said when it comes to decoding
```python
>> import ziproto
>> Data = ziproto.encode({"foo": "bar", "fruits": ['apple', 'banana']})
>> ziproto.decode(Data)
{'foo': 'bar', 'fruits': ['apple', 'banana']}
```

To determine what type of variable you are dealing with, you could use the decoder
```python
>> import ziproto
>> from ziproto.ZiProtoDecoder import Decoder

>> Data = ziproto.encode({"foo": "bar", "fruits": ['apple', 'banana']})
>> SuperDecoder = Decoder(Data)
>> print(SuperDecoder.get_type())
ValueType.MAP
```
