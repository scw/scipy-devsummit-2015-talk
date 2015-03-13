# Use the GitHub API to get information on the usage
# of SciPy packages. kLOCs calculated with `cloc`.
import sys
from pygithub3 import Github

gh = Github()

# name, user, repo, kloc
repositories = (
    ('matplotlib', 'matplotlib', 'matplotlib', 63),
    ('Nose', 'nose-devs', 'nose', 7),
    ('NumPy', 'numpy', 'numpy', 84),
    ('Pandas', 'pydata', 'pandas', 112),
    ('SciPy', 'scipy', 'scipy', 91),
    ('SymPy', 'sympy', 'sympy', 223)
)

unique_logins = set()
total_kloc = 0 
print "Name\tKloc\tcommitters\tstars"
for (name, user, repo, kloc) in repositories:
    contributors = gh.repos.list_contributors(user=user, repo=repo)
    # get the repository object
    r = gh.repos.get(user=user, repo=repo)
    # all committers as login names
    logins = [l.login for l in contributors.all()]
    # update our running totals
    unique_logins.update(logins)
    total_kloc += kloc

    print "[{name}]({homepage})\t{kloc}\t{committers}\t{stars}".format(
        name=name, homepage=r.homepage, kloc=kloc,
        committers=len(logins), stars=r.stargazers_count)

print "Total:\n  {}K lines of code\n  {} contributors.".format(
    total_kloc, len(unique_logins))
