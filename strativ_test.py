
def log_function_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result

    return wrapper


@log_function_execution
def greet(name):
    print(f"Hello, {name}!")


greet("Arif")
#
# Problem
# 3: If
# you
# were
# asked
# to
# write
# a
# text
# editor
# for python from scratch.
# Now, you
# 're tasked with building a syntax highlighter.
# What
# would
# you
# need
# to
# consider
# when
# building
# such
# a
# feature?
# and how
# would
# you
# try implementing it?
# # Talk/Write here
#
# Problem
# 4: Optimize
# the
# following
# code.State
# the
# issue and why
# your
# solution
# works.
#
#
# # Modify the code here
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=150)
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=150)
#
#
# author = models.Foreignkey(Author)
#
# posts = Post.objects.all()
#
# for post in posts:
#     print(post.title, post.author.name)
#
# Problem
# 5:
#
# Read
# API
# docs: https: // openlibrary.org / developers / api
#
# Write
# a
# script
# that
# outputs
# the
# writers, publishing
# year and also
# the
# URL
# of
# the
# cover
# image
# of
# the
# book - Two
# Scoops
# of
# Django
