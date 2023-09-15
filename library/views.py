from django.shortcuts import render, HttpResponse

from .forms import UploadFileForm

from .models import NewBook

# Create your views here.
def UploadFileView(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES["file"] # "File" is the file in UploadFIleForm
        title = request.POST["title"] # Apart from files all other items are obtained using POST

        # Creates a new object in NewBook Model
        newBook = NewBook.objects.create(book = file, bookTitle = title)
        newBook.save()

        return HttpResponse(f"The file {newBook.book} is titled {newBook.bookTitle}")

    else:
        form = UploadFileForm
    return render(request, "library.html", {"form": form})
