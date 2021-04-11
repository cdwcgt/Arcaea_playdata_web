# Arcaea_playdata_web
使用python flask框架+sqlite数据库制作的Arcaea查分记录查询<br/>
.sql内[]自行替换成对应的数据<br/>
文本替换yyy例:
```
.版本 2
.支持库 eAPI

    输出sql ＝ 子文本替换 (#userinfo_sql, “[name]”, 子文本替换 (json.取通用属性 (“content.name”), “'”, “''”, , , 真), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[id]”, duserid, , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[ptt]”, 到文本 (到数值 (json.取属性 (“content.rating”).取数据文本 ()) ÷ 100), , , 真)

    输出sql ＝ 子文本替换 (输出sql, “[user_id]”, duserid, , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[songname]”, 子文本替换 (songname, “'”, “''”, , , 真), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[songdiff]”, diff_s, , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[songrating]”, songrating, , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[score]”, json.取属性 (“content['recent_score'].score”).取数据文本 (), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[getptt]”, 格式化文本 (“%.3f”, 到数值 (json.取属性 (“content['recent_score'].rating”).取数据文本 ())), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[pure]”, json.取属性 (“content['recent_score']['perfect_count']”).取数据文本 (), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[purep]”, json.取属性 (“content['recent_score']['shiny_perfect_count']”).取数据文本 (), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[far]”, json.取属性 (“content['recent_score']['near_count']”).取数据文本 (), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[lost]”, json.取属性 (“content['recent_score']['miss_count']”).取数据文本 (), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[time]”, json.取属性 (“content['recent_score']['time_played']”).取数据文本 (), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[userptt]”, 到文本 (到数值 (json.取属性 (“content.rating”).取数据文本 ()) ÷ 100), , , 真)

    输出sql ＝ 子文本替换 (输出sql, “[score_str]”, 子文本替换 (格式化分数 (json.取属性 (“content['recent_score'].score”).取数据文本 ()), “'”, “''”, , , 真), , , 真)
    输出sql ＝ 子文本替换 (输出sql, “[time_str]”, 时间_时间戳转文本 (json.取属性 (“content['recent_score']['time_played']”).取数据文本 ()), , , 真)

```
