{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d:\\\\shlesh-python'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.chdir('d:/shlesh-python')\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting Calc.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile Calc.py\n",
    "def sumation(a,b):\n",
    "    return a+b\n",
    "def deletion(a,b):\n",
    "    return a-b\n",
    "def multiplication(a,b):\n",
    "    return a*b\n",
    "def divide(a,b):\n",
    "    return a/b\n",
    "x=10\n",
    "y=15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing A1.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile A1.py\n",
    "def find(s,sub):\n",
    "    l=len(sub)\n",
    "    for i,j in enumerate(s):\n",
    "        if s[i:i+l]==sub:\n",
    "            return i\n",
    "def rfind(s,sub):\n",
    "    l=len(sub)\n",
    "    for i,j in enumerate(s):\n",
    "        if s[i:i+l]==sub:\n",
    "            ans=i\n",
    "    return ans\n",
    "def count(s,sub):\n",
    "    l=len(sub)\n",
    "    c=0\n",
    "    for i,j in enumerate(s):\n",
    "        if s[i:i+l]==sub:\n",
    "            c+=1\n",
    "    return c\n",
    "def first(s):\n",
    "    return s.split()[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
