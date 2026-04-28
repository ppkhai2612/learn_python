# io - Core tools for working with streams

This module provides Python’s main facilities for dealing with various types of I/O. There are three main types of I/O: **text I/O**, **binary I/O** and **raw I/O**. A concrete object belonging to any of these categories is called **a file object** (aka  stream and file-like object)

Each concrete stream object will have various capabilities: it can be **read-only**, **write-only**, or **read-write**. It can also allow arbitrary **random access** (seeking forwards or backwards to any location), or only **sequential access** (for example in the case of a socket or pipe)

## Types of I/O

**Text I/O**: expects and produces `str` objects

```python
f = open("myfile.txt", "r", encoding="utf-8")
f = io.StringIO("some initial text data")
```

**Binary I/O** (aka buffered I/O): expects bytes-like objects and produces bytes objects. No encoding, decoding, or newline translation is performed. This category of streams can be used for all kinds of non-text data

```python
f = open("myfile.jpg", "rb")
f = io.BytesIO(b"some initial binary data: \x00\x01")
```

Raw I/O (aka unbuffered I/O): is generally used as a low-level building-block for binary and text streams; it is rarely useful to directly manipulate a raw stream from user code

```python
f = open("myfile.jpg", "rb", buffering=0)
```

## Class hierarchy

```bash
IOBase
|── RawIOBase
|── BufferedIOBase
|── TextIOBase
```

You can read [here](https://docs.python.org/3/library/io.html#class-hierarchy) for more subclasses

## Common useful functions/methods:
- `io.open()`: alias for the builtin `open()` function
- `seek(offset, whence)`: change the stream position to the given byte `offset`, interpreted relative to the position indicated by `whence`
- `tell()`: get the current stream position