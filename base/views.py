from django.shortcuts import render, redirect
# from .forms import SteganographyForm
from .forms import EncodeImageForm
from .models import steganography
from django.conf import settings
import os
from PIL import Image
import numpy as np

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def encode_image(request):
    media_root = settings.MEDIA_ROOT
    if request.method == 'POST':
        form = EncodeImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the form data
            image = request.FILES['image']
            message = form.cleaned_data['message']
            password = form.cleaned_data['password']
            dest = form.cleaned_data['dest']

            # save the instance of a model
            encoded_image = steganography(image=image, message=message, password=password, dest=dest)
            encoded_image.save()
            
            # Encode the image
            image_path = os.path.join(media_root, 'stegoimages', image.name)
            encoded_image_path = os.path.join(media_root, 'stegoimages', dest)
            
            try:
                img = Image.open(image_path)
                width, height = img.size
                array = np.array(list(img.getdata()))

                if img.mode == 'RGB':
                    n = 3
                elif img.mode == 'RGBA':
                    n = 4

                total_pixels = array.size // n

                message += password
                b_message = ''.join([format(ord(i), "08b") for i in message])
                req_pixels = len(b_message)

                if req_pixels > (total_pixels * 3):
                    return render(request, 'error.html', {'message': 'ERROR: Need larger file size'})

                index = 0
                for p in range(total_pixels):
                    for q in range(0, 3):
                        if index < req_pixels:
                            array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                            index += 1

                array = array.reshape(height, width, n)
                enc_img = Image.fromarray(array.astype('uint8'), img.mode)
                enc_img.save(encoded_image_path)
                return redirect('success')
            except Exception as e:
                return render(request, 'base/error.html', {'message': str(e)})
    else:
        form = EncodeImageForm()

    return render(request, 'base/encodeImg.html', {'form': form})


def success(request):
    return render(request, 'base/success.html')

