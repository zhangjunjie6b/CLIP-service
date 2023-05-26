from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

work = pipeline(task=Tasks.multi_modal_embedding,
                        model='damo/multi-modal_clip-vit-base-patch16_zh', model_revision='v1.0.1')
text_embedding = work.forward({'text': "1111"})['text_embedding']