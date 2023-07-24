import video_processing_module
import object_detection_module
import pedestrian_intent_prediction_module
import risk_assessment_module
import text_generation_module

class MainProgram:
    def __init__(self):
        self.video_processor = video_processing_module.VideoProcessor()
        self.object_detector = object_detection_module.ObjectDetector()
        self.pedestrian_predictor = pedestrian_intent_prediction_module.PedestrianIntentPredictor()
        self.risk_assessor = risk_assessment_module.RiskAssessor()
        self.text_generator = text_generation_module.TextGenerator()

    def process_video(self, video_path):
        # Process the video and obtain frames
        frames = self.video_processor.process(video_path)
        return frames

    def detect_objects(self, frames):
        # Detect objects in the frames
        detected_objects = self.object_detector.detect(frames)
        return detected_objects

    def predict_intent(self, detected_objects):
        # Predict pedestrian intents
        pedestrian_intents = self.pedestrian_predictor.predict(detected_objects)
        return pedestrian_intents

    def assess_risk(self, pedestrian_intents):
        # Assess risks based on pedestrian intents
        risk_assessment = self.risk_assessor.assess(pedestrian_intents)
        return risk_assessment

    def generate_text(self, risk_assessment):
        # Generate text from the risk assessment
        text_output = self.text_generator.generate(risk_assessment)
        return text_output

    def run(self, video_path):
        frames = self.process_video(video_path)
        detected_objects = self.detect_objects(frames)
        pedestrian_intents = self.predict_intent(detected_objects)
        risk_assessment = self.assess_risk(pedestrian_intents)
        text_output = self.generate_text(risk_assessment)
        return text_output


if __name__ == "__main__":
    program = MainProgram()
    video_path = 'path_to_your_video'
    text_output = program.run(video_path)
    print(text_output)
