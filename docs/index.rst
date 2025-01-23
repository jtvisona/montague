.. Montague documentation master file, created by
   sphinx-quickstart on Thu Jan 23 12:30:43 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Regular text ``inline code``. 
.. `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

Montague Documentation
======================
Welcome to Montague, the python-centric object-oriented framework for OO development using custom-developed
objects managed through a GUI. This project is found at the github repo: `montague (github.com)<https://github.com/jtvisona/montague>`_.



This project began as an attempt to create a library of objects for the use in a masters thesis in order to explore
the theoretical basis of `sentiment analysis (WP)<https://en.wikipedia.org/wiki/Sentiment_analysis>`. In the course
of a basic exploration of Jupyter notebook, pandas, nltk, and other libraries, it seemed like a good idea to port
some of that functionality outside of the .ipnyb format. The long-term ambition is to build a library of objects
that can be used in NLP projects and be themselves transparent across projects as well as metaprogrammatically
accessible. At the core of the framework is an object management object which will simplify the creation, duplication,
access, and deletion of objects.

Initially, there are two goals for this project. Create the object management basis and put a GUI front-end on it in
Tkinter, but with an eye on moving over to Django. And then to create a series of developer utilitity objects for
logging, documentation, and unit testing. The long-term goal is to quickly assimiliate new objects into the library
and have their language-specific aspects available for NLP projects. At the same time, such a system shall accomodate
educational materials and references as part of the object library.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


