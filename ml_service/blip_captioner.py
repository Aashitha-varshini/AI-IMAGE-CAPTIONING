# BLIP Model Integration for Captioning
# This script loads the BLIP model and provides a function to generate captions for images.

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import io

class BLIPCaptioner:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def generate_caption(self, image_bytes: bytes) -> str:
        try:
            image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

            # Force channels layout to avoid ambiguous shapes (e.g. 1x1 images)
            # Some tiny images make the processor guess the wrong channel dimension
            # which leads to a ValueError. Explicitly specify channels_last.
            inputs = self.processor(image, return_tensors="pt", input_data_format="channels_last")

            out = self.model.generate(**inputs, max_length=15)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            # Optionally post-process for kid-friendly output
            return caption
        except Exception as e:
            # Re-raise a clear exception for the ASGI app to log and return
            raise RuntimeError(f"Caption generation failed: {e}")
