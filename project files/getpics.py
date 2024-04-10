import pandas as pd
import requests
import os

def download_images(excel_file_path, images_dir):
    # 确保images_dir目录存在
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # 读取Excel文件的这2列
    df = pd.read_excel(excel_file_path).loc[:, ['标题', '图片链接']]

    # 遍历DataFrame并下载图片
    for index, row in df.iterrows():
        image_url = row['图片链接']  # 根据你的列名进行调整
        image_name = row['标题'] + '.jpg'  # 确保文件名有正确的扩展名
        if '/' in image_name:
            image_name = image_name.replace("/", "·")
        file_path = os.path.join(images_dir, image_name)

        # 检查文件是否已经存在
        if os.path.exists(file_path):
            print(f"文件已存在，跳过下载: {image_name}")
            continue


        try:
            response = requests.get(image_url)
            response.raise_for_status()  # 确保请求成功
            # 保存图片
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f'下载成功: {image_name}')
        except requests.RequestException as e:
            print(f'下载失败: {image_url}, 错误: {e}')

# 调用函数
if __name__ == "__main__":
    download_images('lists/top250films.xlsx', 'static/films')
    download_images('lists/top250books.xlsx', 'static/books')
    download_images('lists/top250music.xlsx', 'static/music')
