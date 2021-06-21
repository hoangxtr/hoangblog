# CenterNet

## Introduction
- Tính tới hiện tại, một trong những flowchart phổ biến nhất của **Object Detection** là dựa trên anchor box. Cách tiếp cận này thường đòi hỏi 1 lượng lớn *anchor box* để match được IOU và *anchor box* cũng phải được định nghĩa thủ công. *Anchor box* có thể không match *ground truth*, vì vậy gây ảnh hưởng đến nhánh classification.
- **Corner-net** ra đời để khắc phục nhược điểm của anchor-based approach. Đây là **keypoint-based** approach. Mỗi object sẽ được represented by a pair of corner keypoints (top-left and bottom-right). However, performance of this approach **hạn chế** bởi vì miss the global information nên không nhận diện được các cặp tương ứng biểu diễn 1 object.
