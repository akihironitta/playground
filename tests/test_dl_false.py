def test_segfault(datadir, tmpdir):
    import ctypes
    ctypes.string_at(0)  # segfault on purpose
