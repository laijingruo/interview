#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "用法: $0 <搜索文件> <搜索内容> <输出文件>"
    exit 1
fi

search_file="$1"
search_content="$2"
output_file="$3"

if [ ! -f "$search_file" ]; then
    echo "错误: 文件 '$search_file' 不存在"
    exit 1
fi

echo "正在文件 '$search_file' 中搜索 '$search_content'..."
echo "搜索结果:"

grep -n "$search_content" "$search_file" | tee "$output_file"

if [ ! -s "$output_file" ]; then
    echo "没有找到匹配内容"
    rm "$output_file"
else
    match_count=$(wc -l < "$output_file")
    echo "找到 $match_count 处匹配，结果已保存到 '$output_file'"
fi