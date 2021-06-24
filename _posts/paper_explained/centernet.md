# CenterNet

## Introduction
- Tính tới hiện tại, một trong những flowchart phổ biến nhất của **Object Detection** là dựa trên anchor box. Cách tiếp cận này thường đòi hỏi 1 lượng lớn *anchor box* để match được IOU và *anchor box* cũng phải được định nghĩa thủ công. *Anchor box* có thể không match *ground truth*, vì vậy gây ảnh hưởng đến nhánh classification.
- **Corner-net** ra đời để khắc phục nhược điểm của anchor-based approach. Đây là **keypoint-based** approach. Mỗi object sẽ được represented by a pair of corner keypoints (top-left and bottom-right). However, performance of this approach **hạn chế** bởi vì miss the global information nên không nhận diện được các cặp tương ứng biểu diễn 1 object.
- To address **Corner-net**'s issues, tác giả trang bị cho **Corner-net** một output nữa là **Center Keypoints**, trả về  các tâm của object. Tác giả tin rằng: nếu 1 Boundingbox (pair of Top-Left and Bottom-Right) có IoU cao với Ground truth, thì khả năng cao Center Keypoint sẽ nằm trong Central Region of bounding box (Vùng giữa bounding box, cách tìm sẽ được trình bày sau). Do đó, khi inference, sau khi đã có bounding box của object, ta sẽ xác định object có đúng không bằng cách kiểm tra xem có Center Keypoint nào cùng class bên trong object hay không.
- To detect center keypoint and corners tốt hơn, tác giả để xuất phương pháp để tăng cường thông tin của center keypoint và corner đó là **Center pooling** và **Cascade Corner Pooling**: 
    - Center Pooling: 
    - Cascade Corner Pooling

## Approach
