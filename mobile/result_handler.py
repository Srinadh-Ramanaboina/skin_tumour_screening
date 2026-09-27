class ResultHandler:

    @staticmethod
    def process(response_data):

        prediction = response_data.get(
            "prediction"
        )

        confidence = response_data.get(
            "confidence"
        )

        if prediction is None:
            return {
                "status": "error",
                "message": "Prediction was not returned."
            }

        if confidence is None:
            return {
                "status": "error",
                "message": "Confidence was not returned."
            }

        confidence_percent = confidence * 100

        return {
            "status": "success",
            "prediction": prediction,
            "confidence": confidence_percent,
            "message": "Screening result generated."
        }