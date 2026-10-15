from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    # 仅展示已经实现的功能。所有业务指标在相应模型和权限逻辑建成后接入。
    profile = getattr(request.user, "workbench_profile", None)
    role_name = profile.get_role_display() if profile else "未分配（请联系管理员）"
    return render(request, "dashboard/index.html", {"role_name": role_name})
