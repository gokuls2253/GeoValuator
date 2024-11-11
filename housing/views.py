from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import pickle

# Load the saved model from pickle file when the server starts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'housing/ml_model/house_price_model.pkl')

# Load the model from the pickle file
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def project(request):
    return render(request, 'housing/project.html')

def environment(request):
    return render(request, 'housing/environment.html')

def culture(request):
    return render(request, 'housing/culture.html')

@csrf_exempt
def predict_price(request):
    if request.method == 'POST':
        try:
            # Log the request data for debugging
            print("Received POST data:", request.POST)

            # Get data from the request.POST
            total_sqft = request.POST.get('total_sqft')
            size = request.POST.get('size')
            bath = request.POST.get('bath')
            balcony = request.POST.get('balcony')
            location = request.POST.get('location')
            area_type = request.POST.get('area_type')

            # Input validation: Ensure all inputs are provided and valid
            if not (total_sqft and size and bath and balcony and location and area_type):
                print("Missing input data")
                return JsonResponse({'error': 'Missing input data'}, status=400)

            # Ensure numeric fields are properly formatted
            try:
                total_sqft = float(total_sqft)
                size = int(size)
                bath = int(bath)
                balcony = int(balcony)
            except ValueError:
                print("Invalid numeric input")
                return JsonResponse({'error': 'Invalid input. Please provide valid numeric values.'}, status=400)

            
            # # Convert inputs to appropriate types
            # total_sqft = float(total_sqft)
            # size = int(size)
            # bath = int(bath)
            # balcony = int(balcony)

            # Prepare the data in the format expected by the model (with feature names)
            input_data = pd.DataFrame([[total_sqft, size, bath, balcony]], 
                                      columns=['total_sqft', 'size', 'bath', 'balcony'])

            print("All inputs are valid. Preparing to predict.")

            # Make a prediction using the loaded model
            prediction = model.predict(input_data)
            print("Prediction successful:", prediction)

            # Return the predicted price as a JSON response
            return JsonResponse({'predicted_price': prediction[0]})

        except ValueError as e:
            print("ValueError:", e)
            return JsonResponse({'error': 'Invalid input. Please provide numeric values.'}, status=400)
        except Exception as e:
            print("Exception:", e)
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
