## Git Pre-Commit Hooks ##

This folder contains the git "hooks" that I use for my python code repositories.

### To Use ###

  - Place the "pre-commit" file in the .git/hooks/ directory of your project.
  - Place any of the test scripts in the .git/hooks/ directory along with it.
  - Make sure each file is executable (chmod a+x FILENAME)
  - When you attempt to make a commit the pre-commit file will run any of these pre-defined scripts

#### pre-commit ####

Attempts to import and run all the sub-scripts that it can find when a git commit is run. If any of those scripts return an error it will reject the current commit. This file contains only summary and organizational output. Individual test scripts should provide their own output concerning errors.

#### Sub_Scripts ####
  - find_forbidden
  -- Will check files for some python anti-patterns as well as generic code found in un-cleaned debugging code and rejects a commit if it finds it.
  - no_master
  -- Will reject any commit made directly to the master branch. You really should be committing to sub-branches and then submitting pull requests to ensure a clean consistant code base.... So this enforces that on the "frantic fix days."
  - pep8
  -- Will run [pep8](http://legacy.python.org/dev/peps/pep-0008/#introduction) Python style standards on your code and reject a commit that results in errors.
  - timestamp (WARNING: currently only works stand-alone because of unused code stashing process implemented in the pre-commit script)
  -- Gets current time and updates the @changed tag in each commited file that contains it.

#### Create a New Test  ####

I have made adding new tests as easy as possible. Create a python file that contains the following base class. Extend the init and run functions to your hearts desire. Just make sure it returns 0 for success and 1 for failure.

```python

class TestSuite():
    """
	@name TestSuite
	@brief This class contains all the functions needed to implement a series of tests on the files it is passed.
	@errors If this class raises ANY error that it does not handle itself the pre-commit container will handle the error and proceed as if all tests have passed. So, handle all errors you receive internally, and please err on the side of a test passing if you fail at creating a stable test. No need to punish the developer for our mistakes. 
    """
    
    def __init__(self):
	    print("do what you will in your init...")

	def run(self, files):
	"""
	@name run
	@brief This function should run checks on the set of files it contains. Once complete, it should return a 0 if successful and a 1 if it fails.
	@param files An array that contains the full path to the set of files to be tested.

	@example
	    err = 0
        for file_name in files:
            try:
                result = 0
                result = self.check_file(file_name)
                if result == 1:
                    err = 1
            except Exception as _ee:
                pass
        return err	
	"""
	    return 0

```

#### TODO ####

  - Create a config file so that the list of acceptable scripts does not live in the code of the pre-commit file.
  - Create a makefile template that makes this easier for new developers to incorporate into their existing projects.
  - Create documentation around how to incorporate this into testing makefile builds to allow code standard scripts to be passed along with projects
