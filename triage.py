# triage.py
# Reads alerts from alerts.json, scores them, explains why,
# labels them, shows the worst first, and saves a report file.

import json

# ---- Read the alerts from the separate file ----
with open("alerts.json") as f:
    alerts = json.load(f)

# ---- Brain 1: score ----
def score_alert(alert):
    score = 0
    if alert["failed_logins"] >= 100:
        score = score + 50
    elif alert["failed_logins"] >= 5:
        score = score + 20
    if alert["known_bad_ip"] == True:
        score = score + 40
    if alert["hour"] < 6 or alert["hour"] >= 22:
        score = score + 15
    if alert["country"] != "USA":
        score = score + 15
    return score

# ---- Brain 2: reasons ----
def reasons_for(alert):
    reasons = []
    if alert["failed_logins"] >= 100:
        reasons.append("very many failed logins (" + str(alert["failed_logins"]) + ")")
    elif alert["failed_logins"] >= 5:
        reasons.append("several failed logins (" + str(alert["failed_logins"]) + ")")
    if alert["known_bad_ip"] == True:
        reasons.append("known bad IP")
    if alert["hour"] < 6 or alert["hour"] >= 22:
        reasons.append("odd hour (" + str(alert["hour"]) + ":00)")
    if alert["country"] != "USA":
        reasons.append("unexpected country (" + alert["country"] + ")")
    return reasons

# ---- Brain 3: label ----
def label_for(score):
    if score >= 70:
        return "CRITICAL"
    elif score >= 30:
        return "MEDIUM"
    else:
        return "LOW"

# ---- Score every alert ----
for alert in alerts:
    alert["score"] = score_alert(alert)

# ---- Sort so the highest score is first ----
alerts.sort(key=lambda a: a["score"], reverse=True)

# ---- Count how many of each label (for the summary) ----
num_critical = 0
num_medium = 0
num_low = 0
for alert in alerts:
    label = label_for(alert["score"])
    if label == "CRITICAL":
        num_critical = num_critical + 1
    elif label == "MEDIUM":
        num_medium = num_medium + 1
    else:
        num_low = num_low + 1

# ---- Build the report as a list of text lines ----
lines = []
lines.append("================ TRIAGE REPORT ================")
lines.append("Total alerts: " + str(len(alerts)))
lines.append("CRITICAL: " + str(num_critical) + "   MEDIUM: " + str(num_medium) + "   LOW: " + str(num_low))
lines.append("===============================================")
lines.append("")

for alert in alerts:
    label = label_for(alert["score"])
    reasons = reasons_for(alert)

    lines.append(label + " | score " + str(alert["score"]) + " | alert " + alert["id"])
    lines.append("    " + alert["description"])
    if len(reasons) > 0:
        lines.append("    Why: " + ", ".join(reasons))
    else:
        lines.append("    Why: nothing suspicious")
    lines.append("")

# ---- Print the report to the screen ----
for line in lines:
    print(line)

# ---- Save the report to a file called report.txt ----
with open("report.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")

print("Report saved to report.txt")