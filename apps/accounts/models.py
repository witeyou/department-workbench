"""当前只实现角色档案；未来对象级权限须在查询与服务层额外校验。"""
from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "系统管理员"
        LEADER = "leader", "部门领导"
        MARKET_LEAD = "market_lead", "市场负责人"
        MARKET = "market", "市场人员"
        RND_LEAD = "rnd_lead", "研发负责人"
        RND = "rnd", "研发人员"
        QA = "qa", "测试人员"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workbench_profile",
    )
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.RND)
    department = models.CharField(max_length=80, blank=True, default="")

    def __str__(self) -> str:
        return f"{self.user.username} / {self.get_role_display()}"
