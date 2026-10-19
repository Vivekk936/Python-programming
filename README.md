# Python Programming

A collection of Python learning examples, practice scripts, Jupyter notebooks, and a small Streamlit demo. Topics range from core Python and object-oriented programming to data analysis and visualization.

## Repository layout

| Folder | Contents |
| --- | --- |
| `Basic Concept/` | Core Python examples, including classes, functions, exceptions, dictionaries, regular expressions, JSON/pickle, and Tkinter |
| `OOPs/` | Object-oriented programming examples such as inheritance, polymorphism, and magic methods |
| `Numpy/` | NumPy arrays, indexing, operations, statistics, and reshaping |
| `Pandas/` | Series and DataFrame examples, indexing, and filtering; includes notebooks and CSV datasets |
| `Matplolib/` | Matplotlib notebooks demonstrating charts such as bar, histogram, pie, and scatter plots |
| `seaborn/` | Seaborn visualization notebooks for relational, categorical, distribution, matrix, and regression plots |
| `Streamlit/` | A Streamlit example app with basic widgets and CSV upload |

Some folders contain their own datasets and notebooks. The scripts and notebooks are independent exercises rather than one integrated application.

## Getting started

Use Python 3. To work with the notebooks, install Jupyter; install the libraries used by the examples as needed:

```powershell
python -m pip install jupyter numpy pandas matplotlib seaborn streamlit
```

Start Jupyter from the repository root:

```powershell
python -m jupyter lab
```

Run an individual Python example from the repository root, for example:

```powershell
python "Basic Concept\Inheritance.py"
```

Run the Streamlit demo:

```powershell
python -m streamlit run "Streamlit\app.py"
```

The demo displays basic text and widgets and lets you upload a CSV or text file to preview its first five rows. Other scripts may require only Python or a subset of the packages above.
