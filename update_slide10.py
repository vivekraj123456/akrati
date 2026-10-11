import re
import base64

with open('anjana_full_profile_feed.png', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')
data_uri = f'data:image/png;base64,{img_b64}'

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    s10_start = content.find('id="10"')
    if s10_start == -1:
        print(f'Slide 10 not found in {filename}')
        return
    s11_start = content.find('id="11"', s10_start)
    if s11_start == -1:
        print(f'Slide 11 not found in {filename}')
        return

    s10_block = content[s10_start:s11_start]

    # Find data-node-path="0" and data-node-path="1" inside slide 10
    node0_idx = s10_block.find('data-node-path="0"')
    node1_idx = s10_block.find('data-node-path="1"')
    if node0_idx == -1 or node1_idx == -1:
        print(f'Nodes not found in {filename}')
        return

    # Replace node 0 section
    # Desired node 0:
    new_node0 = (
        'data-node-path="0" style="display: flex; flex-direction: column; align-items: stretch; gap: 0px; '
        'min-width: 560px; min-height: 840px; flex-grow: 0; flex-shrink: 0; max-width: 560px; max-height: 840px; '
        'height: 840px; background-color: rgb(255, 251, 244); border-width: 8px; border-style: solid; '
        'border-color: rgb(255, 251, 244); border-radius: 120px 120px 30px 30px; '
        'box-shadow: rgba(60, 40, 20, 0.35) 0px 30px 64px 0px; transform: rotate(2deg); overflow: hidden; box-sizing: border-box;">'
        '<div data-node-path="0.0" style="position: relative; width: 100%; height: 100%; overflow: hidden; '
        'background-color: rgb(255, 255, 255); border-radius: 112px 112px 22px 22px;">'
        f'<img src="{data_uri}" alt="Instagram profile and feed design for Anjana&#39;s Glam Hub" draggable="false" '
        'style="width: 100%; height: 100%; display: block; object-fit: cover; object-position: center top;">'
        '</div></div><'
    )

    old_node0 = s10_block[node0_idx:node1_idx]
    updated_s10_block = s10_block[:node0_idx] + new_node0 + s10_block[node1_idx:]

    new_content = content[:s10_start] + updated_s10_block + content[s11_start:]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Successfully updated {filename}')

update_file('index.html')
update_file('Akrati Koshta Portfolio.html')
