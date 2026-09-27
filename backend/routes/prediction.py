
from flask import Blueprint, request, jsonify
import os
import sys




project_root = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

# Allow Python to find project folders
sys.path.insert(0, project_root)




from model.inference import SkinModel
from image_processing.image_validator import ImageValidator



prediction_bp = Blueprint(
    "prediction",
    __name__
)




skin_model = SkinModel()




@prediction_bp.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:


        if "image" not in request.files:

            return jsonify({
                "status": "error",
                "error_type": "missing_image",
                "message": "No image was provided."
            }), 400




        image = request.files["image"]




        if not image.filename:

            return jsonify({
                "status": "error",
                "error_type": "empty_filename",
                "message": "No image was selected."
            }), 400




        upload_folder = os.path.join(
            project_root,
            "uploads"
        )

        os.makedirs(
            upload_folder,
            exist_ok=True
        )




        image_path = os.path.join(
            upload_folder,
            "input.jpg"
        )

        image.save(
            image_path
        )


        validation = ImageValidator.validate(
            image_path
        )


        if not validation["valid"]:

            return jsonify({
                "status": "error",
                "error_type": "invalid_image",
                "message": validation["message"]
            }), 400




        try:

            prediction, confidence = (
                skin_model.predict(
                    image_path
                )
            )

        except Exception as model_error:

            print(
                "MODEL ERROR:",
                model_error
            )

            return jsonify({
                "status": "error",
                "error_type": "model_error",
                "message": (
                    "Unable to process the image "
                    "with the prediction model."
                )
            }), 500


       

        return jsonify({

            "status": "success",

            "prediction": int(
                prediction
            ),

            "confidence": float(
                confidence
            ),

            "image": {

                "format": validation[
                    "format"
                ],

                "width": validation[
                    "width"
                ],

                "height": validation[
                    "height"
                ]

            }

        }), 200


    

    except Exception as error:

        print(
            "SERVER ERROR:",
            error
        )

        return jsonify({

            "status": "error",

            "error_type": "server_error",

            "message": (
                "An unexpected server error occurred."
            )

        }), 500

