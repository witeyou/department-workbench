# 初始迁移：随启动工程一起提交，之后请用 makemigrations 生成增量迁移。
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("role", models.CharField(choices=[("admin", "系统管理员"), ("leader", "部门领导"), ("market_lead", "市场负责人"), ("market", "市场人员"), ("rnd_lead", "研发负责人"), ("rnd", "研发人员"), ("qa", "测试人员")], default="rnd", max_length=20)),
                ("department", models.CharField(blank=True, default="", max_length=80)),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="workbench_profile", to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
