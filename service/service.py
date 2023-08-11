import torch
from modelscope.utils.constant import Tasks
from modelscope.pipelines import pipeline
from modelscope.preprocessors.image import load_image
from concurrent import futures
import pb.image_pb2 as Impb
import pb.image_pb2_grpc as IMrpc
import numpy as np
import grpc

class ImgHandle(IMrpc.ImgHandleServicer):

    def ImgToVector(self, request, context):

        input_img = load_image(request.Url)
        img_embedding = work.forward({'img': input_img})['img_embedding']
        img_embedding_cpu = img_embedding.cpu()  # 将张量复制到主机内存
        numpy_array = img_embedding_cpu.numpy()
        np.set_printoptions(suppress=True)
        array_string = np.array2string(numpy_array, separator=',')
        # 去除字符串中的换行符和空格
        array_string = array_string.replace('\n', '').replace(' ', '')

        return Impb.Reply(jsonData= array_string)

    def TextToVector(self, textRequest, context):
        text_embedding = work.forward({'text': textRequest.Content})['text_embedding']
        text_embedding = text_embedding.cpu()  # 将张量复制到主机内存
        numpy_array = text_embedding.numpy()
        np.set_printoptions(suppress=True)
        array_string = np.array2string(numpy_array, separator=',')
        # 去除字符串中的换行符和空格
        array_string = array_string.replace('\n', '').replace(' ', '')
        print(array_string)
        return Impb.Reply(jsonData= array_string)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))

    IMrpc.add_ImgHandleServicer_to_server(ImgHandle(), server)
    server.add_insecure_port('0.0.0.0:50051')
    print("成功监听")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    work = pipeline(task=Tasks.multi_modal_embedding,
                        model='damo/multi-modal_clip-vit-base-patch16_zh', model_revision='v1.0.1')
    serve()