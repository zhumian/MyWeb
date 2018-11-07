def response(success=True, data=None, msg="操作成功"):
    return dict(success=success, data=data, msg=msg)
