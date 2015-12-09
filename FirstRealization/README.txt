
по nose:
Установить pip(если нету):
http://pip.readthedocs.org/en/stable/installing/

Установить nose
pip install nose


Now you can run tests for your project:

cd path/to/project
nosetests filename.py


You should see output something like this:

..................................
----------------------------------------------------------------------
Ran 34 tests in 1.440s

OK

(-v option for more details)

HУЖНО ПРОЧИТАТЬ:
http://pythontesting.net/framework/nose/nose-introduction/
http://nose.readthedocs.org/en/latest/usage.html



The easiest fixtures to add are:

setup_module() function: runs before anything else in the file
teardown_module() function: runs after everything else in the file
And if you use a class to define some tests:

setup() method: runs before every test method
teardown() method: runs after every test method


html report:
pip install nose-htmloutput
pip install nose-html-reporting


так работает html:
nosetests -v myfile.py --with-html

nosetests -v myfile.py --with-html --html-file=l.html

nosetests -v myfile.py --with-html --html-file=l.html --html-report-template=report.html

nosetests -v myfile.py --config=example_cfg.ini



вот про джинджа:
http://jinja.pocoo.org/docs/dev/ --config









