import requests
import time
from urllib.parse import quote_plus

def search_paper_links():
    # 论文列表
    papers = [
        "Large Language Models for Automated Data Science: Current Capabilities and Future Directions",
        "A Survey on Large Language Models for Recommendation",
        "Large Language Models Meet Recommendation Systems: A Survey",
        "Large Language Models for Knowledge Graph Completion: A Survey",
        "Large Language Models for Code Generation: A Survey",
        "Large Language Models for Natural Language Processing: A Survey",
        "Large Language Models for Computer Vision: A Survey",
        "Large Language Models for Robotics: A Survey",
        "Large Language Models for Healthcare: A Survey",
        "Large Language Models for Education: A Survey"
    ]
    
    print("搜索论文PDF链接...")
    print("=" * 50)
    
    for i, paper in enumerate(papers, 1):
        print(f"\n{i}. 搜索论文: {paper}")
        
        # 构建搜索URL
        search_query = quote_plus(paper + " PDF")
        search_url = f"https://www.google.com/search?q={search_query}"
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(search_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # 简单的链接提取
                text = response.text.lower()
                if 'pdf' in text:
                    print(f"   找到PDF相关内容")
                    # 提取可能的PDF链接
                    lines = response.text.split('\n')
                    for line in lines:
                        if 'pdf' in line.lower() and 'http' in line:
                            print(f"   可能的链接: {line[:100]}...")
                            break
                else:
                    print(f"   未找到PDF链接")
            else:
                print(f"   搜索失败，状态码: {response.status_code}")
                
        except Exception as e:
            print(f"   搜索出错: {str(e)}")
        
        # 避免请求过于频繁
        time.sleep(2)
    
    print("\n" + "=" * 50)
    print("搜索完成！")

if __name__ == "__main__":
    search_paper_links() 