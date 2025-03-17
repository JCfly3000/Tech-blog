#!/usr/bin/env python
# coding: utf-8

# ---
# title: "Python code optimization with ruff"
# author: "Tony D"
# execute:
#   warning: false
#   error: false
# 
#   
# date: "2025-03-14"
# categories: 
#   - Tool
#   - Python
#   
# image: "images.png"
# jupyter: python3
# ---
# 
# -   ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
# 
# -   🐍 Installable via `pip`
# 
# -   🛠️ `pyproject.toml` support
# 
# ![](images/clipboard-548506117.png)
# 
# # install
# 
# ```{bash}
# #| eval: false
# pip install ruff
# ```
# 
# # check
# 
# before correct python file
# 
# ``` {.python filename="playing.py"}
# #| eval: false
# 
# 
# 
# 
# import pandas
# 
# from importlib.metadata import version
# 
# print('test.py is running')
# print('version is :')
# print(version('rich'))
# 
# a=3+1
# 
# 
# a
# 
# 
# ```
# 
# ```{bash}
# ruff check playing.py
# ```
# 
# # fix

# In[ ]:


#| eval: false
get_ipython().system('ruff check playing.py --fix')


# after fix
# 
# ``` {.python filename="playing.py"}
# #| eval: false
# 
# 
# 
# 
# 
# from importlib.metadata import version
# 
# print('test.py is running')
# print('version is :')
# print(version('rich'))
# 
# a=3+1
# 
# 
# a
# 
# 
# 
# 
# ```
# 
# 
# # format
# 
# 
# 
# ```{bash}
# ruff format playing.py
# ```
# 
# 
# after format
# 
# ``` {.python filename="playing.py"}
# #| eval: false
# from importlib.metadata import version
# 
# print("test.py is running")
# print("version is :")
# print(version("rich"))
# 
# a = 3 + 1
# 
# 
# a
# 
# ```
# 
# # convert .qmd to .py
# 
# ruff only work on .py file, So if want to use ruff to check .qmd file then it need to convert to .py first.
# 
# 
# 
# ```{.python filename='Terminal'}
# #| eval: false
# quarto convert index.qmd    # → index.ipynb
# ```
# 
# ```{.python filename='Terminal'}
# #| eval: false
# jupyter nbconvert --to python index.ipynb    # → index.py
# ```
# 
# then check .py with ruff

# In[ ]:


#| eval: false
get_ipython().system('ruff check index.py')


# # reference:
# 
# https://github.com/astral-sh/ruff
