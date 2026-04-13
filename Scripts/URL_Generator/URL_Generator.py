# url_generator.py

def main():
    print("=== Simple URL Generator ===\n")
    
    # Get user inputs
    prepend = input("Enter the prepend URL (e.g. https://gelbooru.com/index.php?page=post&s=view&id=): ").strip()
    start = int(input("Enter start ID (e.g. 1): "))
    end = int(input("Enter end ID (e.g. 100): "))
    filename = input("Enter output filename (default: urls.txt): ").strip() or "urls.txt"
    
    # Generate URLs and save to file
    urls = []
    for i in range(start, end + 1):
        url = f"{prepend}{i}"
        urls.append(url)
    
    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url + "\n")
    
    print(f"\n✅ Done! Generated {len(urls)} URLs and saved to '{filename}'")

if __name__ == "__main__":
    main()