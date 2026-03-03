# API 통신오류로 수정
    data = json.loads(r.text)
    result_data = data.get('message', {}).get('result') or data.get('result', {})
    html = result_data.get('html', '')
    result = {
        'result': True,
        'original': text,
        'checked': _remove_tags(html),
        'errors': result_data.get('errata_count', 0),  # ← 수정
        'time': passed_time,
        'words': OrderedDict(),