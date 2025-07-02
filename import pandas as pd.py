PS C:\Users\emonc> & "C:/Program Files/Python313/python.exe" "c:/PCA data analysis/import pandas as pd.py"
Traceback (most recent call last):
  File "c:\PCA data analysis\import pandas as pd.py", line 32, in <module>
    plt.bar(range(1, 3), pca.explained_variance_ratio_, alpha=0.7)
    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\emonc\AppData\Roaming\Python\Python313\site-packages\matplotlib\pyplot.py", line 2981, in bar
    return gca().bar(
           ~~~~~~~~~^
        x,
        ^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "C:\Users\emonc\AppData\Roaming\Python\Python313\site-packages\matplotlib\__init__.py", line 1521, in inner
    return func(
        ax,
        *map(cbook.sanitize_sequence, args),
        **{k: cbook.sanitize_sequence(v) for k, v in kwargs.items()})
  File "C:\Users\emonc\AppData\Roaming\Python\Python313\site-packages\matplotlib\axes\_axes.py", line 2572, in bar
    x, height, width, y, linewidth, hatch = np.broadcast_arrays(
                                            ~~~~~~~~~~~~~~~~~~~^
        # Make args iterable too.
        ^^^^^^^^^^^^^^^^^^^^^^^^^
        np.atleast_1d(x), height, width, y, linewidth, hatch)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\emonc\AppData\Roaming\Python\Python313\site-packages\numpy\lib\_stride_tricks_impl.py", line 544, in broadcast_arrays
    shape = _broadcast_shape(*args)
  File "C:\Users\emonc\AppData\Roaming\Python\Python313\site-packages\numpy\lib\_stride_tricks_impl.py", line 419, in _broadcast_shape
    b = np.broadcast(*args[:32])
ValueError: shape mismatch: objects cannot be broadcast to a single shape.  Mismatch is between arg 0 with shape (2,) and arg 1 with shape (3,).

plt.bar(range(1, 3), pca.explained_variance_ratio_, alpha=0.7)
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Variance Explained by Principal Components')

plt.tight_layout()
plt.show()

