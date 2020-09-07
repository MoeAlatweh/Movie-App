from django.shortcuts import render, redirect
<<<<<<< HEAD
from .models import Movie
from django.contrib import messages


def home_page(request):
    user_query = str(request.GET.get('query', ''))
=======
# to import Movie model we create from .modelss
from .models import Movie
# import messages library from django
from django.contrib import messages

# that's way for django
def home_page(request):
    # to take your text when you search the movie you want by using
    user_query = str(request.GET.get('query', ''))
    # to can search in the database, use name__icontains filter to be able use capital or small letter or part of the word you looking for
>>>>>>> step_0_start
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_result': search_result}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)

<<<<<<< HEAD

def create(request):
=======
def create(request):

>>>>>>> step_0_start
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
<<<<<<< HEAD
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            
            response = Movie.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                rating=data.get('rating'),
                notes=data.get('notes'),

            )
            messages.success(request, 'New movie added: {}'.format(data.get('name')))
        except Exception as e:
            messages.warning(
                request, 'Got an error when trying to create new movie: {}'.format(e))
    return redirect('/')

def edit(request, movie_id):
=======
            # ********
            ## 'trailer': request.POST.get('trailer'),
            # ********
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes'),
        }
        # use try and except below to make sure our app not crashing
        try:
            print(request.POST)
            response = Movie.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                # **********
                ## trailer=data.get('trailer'),
                # **********
                rating=data.get('rating'),
                notes=data.get('notes'),
            )
            # massage will pop up when create new movie
            messages.success(request,"New Movie Added: {}".format(data.get('name')))
        except Exception as e:
            messages.warning(request,"Got an error when trying to create new movie: {}".format(e))
    return redirect('/')

def edit(request , movie_id) :
>>>>>>> step_0_start
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
<<<<<<< HEAD
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
=======
            # **********
            ## 'trailer': request.POST.get('trailer'),
            # **********
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes'),
        }
        # we create variable(movie_obj) and make it take id of the movie
>>>>>>> step_0_start
        try:
            movie_obj = Movie.objects.get(id=movie_id)
            movie_obj.name = data.get('name')
            movie_obj.picture = data.get('picture')
<<<<<<< HEAD
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            movie_obj.save()
            messages.success(request, f"Movie updated - {data.get('name')}")
        except Exception as e:
            messages.warning(
                request, 'Got an error when trying to update movie: {}'.format(e))
        return redirect('/')
=======
            # **********
            ## movie_obj.trailer = data.get('trailer')
            # **********
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            # need to make sure to save the adjustments you made
            movie_obj.save()
            # massage will pop up when updating movie
            messages.success(request, "Movie Updated: {}".format(data.get('name')))
        except Exception as e:
            messages.warning(request,f"Got an error when trying to update movie {data.get('name')}")
    return redirect('/')
>>>>>>> step_0_start

def delete(request, movie_id):
    try:
        movie_obj = Movie.objects.get(id=movie_id)
<<<<<<< HEAD
        movie_name = movie_obj.name
        movie_obj.delete()
        messages.warning(request, 'Deleted movie: {}'.format(movie_name))
    except Exception as e:
        messages.warning(request, 'Got an error when trying to delete a movie: {}'.format(e))
    return redirect('/')
=======
        movie_name= movie_obj.name
        movie_obj.delete()
        messages.success(request, "Movie Deleted: {}".format(movie_name))
    except Exception as e:
        messages.warning(request, "Got an error when trying to delete a movie: {}".format(movie_name))
    return redirect('/')


#def trailer(request, movie_id):
 #   data = {
  #      'trailer': request.POST.get('trailer'),
   # }
    #try:
    #
     #   movie_obj = Movie.trailer.get(id=movie_id)
      #  movie_name= movie_obj.name
       # movie_obj.trailer = data.get('trailer')
        ##messages.success(request, "Movie Deleted: {}".format(movie_name))
    #except Exception as e:
     #   pass
        #messages.warning(request, "Got an error when trying to delete a movie: {}".format(movie_name))
    #return redirect('/')

>>>>>>> step_0_start
