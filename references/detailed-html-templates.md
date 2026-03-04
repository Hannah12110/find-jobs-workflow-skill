# Detailed HTML Templates

Use these full templates when generating final artifacts. Replace all placeholders like `[公司名称]`.

## 1) 面试前备考指南（HTML）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>面试备考指南</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f6f8fb; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 28px; border-radius: 12px; margin-bottom: 20px; }
        .header h1 { margin: 0; font-size: 28px; }
        .meta p { margin: 6px 0; opacity: 0.95; }
        .section { background: #fff; border-radius: 12px; padding: 22px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .section h2 { margin-top: 0; color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 8px; }
        .badge { display: inline-block; padding: 3px 10px; border-radius: 999px; font-size: 12px; margin-right: 6px; }
        .badge.source { background: #e3f2fd; color: #1565c0; }
        .badge.high { background: #ffebee; color: #c62828; }
        .badge.medium { background: #fff3e0; color: #e65100; }
        .badge.low { background: #e8f5e9; color: #2e7d32; }
        .q-item { border: 1px solid #e8e8e8; border-radius: 10px; padding: 16px; margin-bottom: 12px; }
        .star { background: #f3e5f5; border-left: 4px solid #9c27b0; border-radius: 8px; padding: 12px; margin-top: 10px; }
        .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        @media (max-width: 768px) { .grid2 { grid-template-columns: 1fr; } }
        ul { margin-top: 8px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎯 面试备考指南</h1>
        <div class="meta">
            <p><strong>公司：</strong>[公司名称]</p>
            <p><strong>岗位：</strong>[岗位名称]</p>
            <p><strong>轮次：</strong>[一面/二面/终面/通用]</p>
            <p><strong>生成时间：</strong>[YYYY-MM-DD HH:mm]</p>
        </div>
    </div>

    <div class="section">
        <h2>🧾 简历亮点清单（必含）</h2>
        <ul>
            <li><strong>技术亮点：</strong>[亮点描述]（对应项目：[项目名]，可关联题：[题型]）</li>
            <li><strong>业务亮点：</strong>[亮点描述]（对应项目：[项目名]，可关联题：[题型]）</li>
            <li><strong>管理/创新亮点：</strong>[亮点描述]（对应经历：[经历]，可关联题：[题型]）</li>
        </ul>
    </div>

    <div class="section">
        <h2>📌 简历与岗位匹配度</h2>
        <p><strong>整体匹配度：</strong>[1-10分]</p>
        <div class="grid2">
            <div>
                <h3>✅ 高匹配项</h3>
                <ul><li>[高匹配项1]</li><li>[高匹配项2]</li></ul>
            </div>
            <div>
                <h3>⚠️ 低匹配项</h3>
                <ul><li>[低匹配项1]</li><li>[低匹配项2]</li></ul>
            </div>
        </div>
        <h3>🎯 备考策略</h3>
        <ul><li>[如何放大优势]</li><li>[如何解释短板]</li></ul>
    </div>

    <div class="section">
        <h2>💡 高频题库（按优先级）</h2>
        <div class="q-item">
            <h3>Q1. [题目]</h3>
            <p>
                <span class="badge source">来源：[小红书/知乎/牛客/LeetCode]</span>
                <span class="badge high">频率：高频</span>
            </p>
            <p><strong>考察意图：</strong>[技术深度/项目拆解/行为能力/文化匹配]</p>
            <div class="star">
                <p><strong>STAR参考回答：</strong></p>
                <p><strong>S：</strong>[情境]</p>
                <p><strong>T：</strong>[任务]</p>
                <p><strong>A：</strong>[行动]</p>
                <p><strong>R：</strong>[结果+数据]</p>
                <p><strong>关键得分点：</strong>[点1/点2/点3]</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>🎭 面试官风格分析</h2>
        <ul>
            <li><strong>一面：</strong>[风格总结]</li>
            <li><strong>二面：</strong>[风格总结]</li>
            <li><strong>终面：</strong>[风格总结]</li>
        </ul>
    </div>

    <div class="section">
        <h2>✅ 备考清单</h2>
        <ul>
            <li>[必备知识点]</li>
            <li>[必备项目案例]</li>
            <li>[必备软技能]</li>
            <li>[避坑项]</li>
        </ul>
    </div>

    <div class="section">
        <h2>🧭 事实与推断</h2>
        <p><strong>事实：</strong>[来自用户输入/简历的事实]</p>
        <p><strong>推断：</strong>[基于数据的推断]</p>
        <p><strong>仍需补充数据：</strong>[缺失的关键指标]</p>
    </div>
</body>
</html>
```

## 2) 面试后复盘报告（HTML）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>面试复盘报告</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f6f8fb; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; padding: 28px; border-radius: 12px; margin-bottom: 20px; }
        .section { background: #fff; border-radius: 12px; padding: 22px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .section h2 { margin-top: 0; color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 8px; }
        .qa { border: 1px solid #e6e6e6; border-radius: 10px; padding: 16px; margin-bottom: 12px; }
        .intent { display: inline-block; background: #e3f2fd; color: #1565c0; border-radius: 999px; padding: 4px 10px; font-size: 12px; }
        .score { display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0; }
        .chip { background: #f0f0f0; border-radius: 999px; padding: 4px 10px; font-size: 12px; }
        .warn { background: #fff3e0; border-left: 4px solid #ff9800; padding: 12px; border-radius: 8px; }
        .ok { background: #e8f5e9; border-left: 4px solid #4caf50; padding: 12px; border-radius: 8px; margin-top: 10px; }
        .star { background: #f3e5f5; border-left: 4px solid #9c27b0; padding: 12px; border-radius: 8px; margin-top: 10px; }
        .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .before { background: #ffebee; padding: 12px; border-radius: 8px; }
        .after { background: #e8f5e9; padding: 12px; border-radius: 8px; }
        @media (max-width: 768px) { .grid2 { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="header">
        <h1>📋 面试复盘报告</h1>
        <p><strong>公司：</strong>[公司]</p>
        <p><strong>岗位：</strong>[岗位]</p>
        <p><strong>轮次：</strong>[轮次]</p>
        <p><strong>生成时间：</strong>[YYYY-MM-DD HH:mm]</p>
    </div>

    <div class="section">
        <h2>💬 问答逐题复盘</h2>
        <div class="qa">
            <h3>问题：[面试官问题]</h3>
            <p><strong>你的回答：</strong>[用户回答]</p>
            <span class="intent">考察意图：[技术/软技能/思维/场景/文化]</span>
            <div class="score">
                <span class="chip">准确性：[x/5]</span>
                <span class="chip">完整性：[x/5]</span>
                <span class="chip">逻辑性：[x/5]</span>
                <span class="chip">表达力：[x/5]</span>
                <span class="chip">匹配度：[x/5]</span>
            </div>
            <div class="warn">
                <strong>存在问题：</strong>
                <ul><li>[问题1]</li><li>[问题2]</li></ul>
            </div>
            <div class="ok">
                <strong>改进建议：</strong>
                <ul><li>[建议1]</li><li>[建议2]</li></ul>
            </div>
            <div class="star">
                <strong>STAR优化回答：</strong>
                <p><strong>S：</strong>[...]</p>
                <p><strong>T：</strong>[...]</p>
                <p><strong>A：</strong>[...]</p>
                <p><strong>R：</strong>[...]</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>🧪 简历问题诊断与修改建议（核心）</h2>
        <h3>五维诊断</h3>
        <ul>
            <li>数据缺失问题：[诊断]</li>
            <li>技术深度不足：[诊断]</li>
            <li>成果闭环不完整：[诊断]</li>
            <li>竞争优势不突出：[诊断]</li>
            <li>逻辑结构问题：[诊断]</li>
        </ul>

        <h3>修改前后对比</h3>
        <div class="grid2">
            <div class="before">
                <h4>❌ 修改前</h4>
                <p>[原始描述]</p>
            </div>
            <div class="after">
                <h4>✅ 修改后（推荐）</h4>
                <p>[优化描述：含数据+技术细节+业务影响]</p>
            </div>
        </div>

        <h3>数据补充清单</h3>
        <ul><li>[需补充数据1]</li><li>[需补充数据2]</li></ul>

        <h3>2分钟自我介绍优化</h3>
        <p>[问题 -> 行动 -> 结果，关键数据前置]</p>
    </div>

    <div class="section">
        <h2>✅ 简历修改检查清单</h2>
        <ul>
            <li>☐ 所有项目有量化数据</li>
            <li>☐ 技术经验展示了工具+场景+方法+效果</li>
            <li>☐ 项目成果形成闭环</li>
            <li>☐ 有平台/工具对比分析</li>
            <li>☐ 有质量体系说明</li>
            <li>☐ 有商业化/增长思维体现</li>
            <li>☐ 自我介绍可在2分钟内完成且数据前置</li>
            <li>☐ 简历关键词与目标岗位匹配</li>
        </ul>
    </div>

    <div class="section">
        <h2>🧭 事实与推断</h2>
        <p><strong>事实：</strong>[...]</p>
        <p><strong>推断：</strong>[...]</p>
        <p><strong>仍需补充数据：</strong>[...]</p>
    </div>
</body>
</html>
```

## 3) 多次面试聚合：个人备考指南（HTML）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>个人备考指南</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f6f8fb; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; padding: 28px; border-radius: 12px; margin-bottom: 20px; }
        .section { background: #fff; border-radius: 12px; padding: 22px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; }
        .card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; border-radius: 10px; padding: 14px; text-align: center; }
        .card .n { font-size: 28px; font-weight: 700; }
        .topic { border: 1px solid #e8e8e8; border-radius: 10px; padding: 14px; margin-bottom: 10px; }
        .pill { display: inline-block; border-radius: 999px; padding: 3px 10px; font-size: 12px; margin-right: 6px; }
        .p-red { background: #ffebee; color: #c62828; }
        .p-orange { background: #fff3e0; color: #e65100; }
        .p-green { background: #e8f5e9; color: #2e7d32; }
        .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
        .box { border-radius: 10px; padding: 12px; background: #fafafa; }
        @media (max-width: 768px) { .grid3 { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 个人备考指南</h1>
        <p><strong>分析基于：</strong>[N]次面试记录</p>
        <p><strong>目标岗位：</strong>[岗位]</p>
        <p><strong>生成时间：</strong>[YYYY-MM-DD HH:mm]</p>
    </div>

    <div class="section">
        <h2>📈 数据概览</h2>
        <div class="cards">
            <div class="card"><div class="n">[N]</div><div>面试次数</div></div>
            <div class="card"><div class="n">[N]</div><div>涉及公司</div></div>
            <div class="card"><div class="n">[N]</div><div>问题总数</div></div>
            <div class="card"><div class="n">[N]</div><div>高频考点</div></div>
        </div>
    </div>

    <div class="section">
        <h2>🎯 高频考点清单</h2>
        <div class="topic">
            <h3>[考点名称]</h3>
            <p><span class="pill p-red">出现[次数]次</span><span class="pill p-orange">掌握：弱/中</span></p>
            <p><strong>考察意图：</strong>[...]</p>
            <p><strong>涉及问题：</strong>[问题列表]</p>
            <p><strong>你的表现：</strong>[短评]</p>
        </div>
    </div>

    <div class="section">
        <h2>🔍 SWOT</h2>
        <div class="grid3">
            <div class="box"><h3>💪 Strengths</h3><ul><li>[...]</li></ul></div>
            <div class="box"><h3>⚠️ Weaknesses</h3><ul><li>[...]</li></ul></div>
            <div class="box"><h3>🚀 Next Actions</h3><ul><li>[...]</li></ul></div>
        </div>
    </div>

    <div class="section">
        <h2>📋 个人化备考计划</h2>
        <ul>
            <li><strong>紧急：</strong>[高频且薄弱项]</li>
            <li><strong>重点巩固：</strong>[中频提升项]</li>
            <li><strong>长期：</strong>[软技能/知识盲区]</li>
        </ul>
    </div>

    <div class="section">
        <h2>🧭 事实与推断</h2>
        <p><strong>事实：</strong>[...]</p>
        <p><strong>推断：</strong>[...]</p>
        <p><strong>仍需补充数据：</strong>[...]</p>
    </div>
</body>
</html>
```

## 4) 模拟面试反馈（文本模板）

```plaintext
🎤 模拟面试反馈

【评分】
准确性：3/5
完整性：2/5
逻辑性：3/5
表达力：4/5
匹配度：3/5

【存在的问题】
1. 回答不够具体，缺少数据和案例支撑
2. 没有使用STAR结构，逻辑不够清晰
3. 缺少对技术细节的深入分析

【改进建议】
1. 补充具体场景和项目案例
2. 使用STAR法则重组回答
3. 增加技术深度，说明原理和取舍

【标准回答参考】
Situation：...
Task：...
Action：...
Result：...

【事实与推断】
- 事实：...
- 推断：...
- 仍需补充数据：...
```
