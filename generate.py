import json
from datetime import date,timedelta,datetime,timezone
from pathlib import Path
p=Path(__file__).resolve().parent
es=json.loads((p/'events.json').read_text())
def esc(s):return s.replace('\\','\\\\').replace('\n','\\n').replace(';','\\;').replace(',','\\,')
def fold(s):
 out=[]; line=''
 for c in s:
  if len((line+c).encode())>75:out.append(line);line=' '
  line+=c
 return '\r\n'.join(out+[line])
now=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
lines=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//School Calendar//JP','CALSCALE:GREGORIAN','METHOD:PUBLISH','X-WR-CALNAME:長野工業高校 1学年（非公式）']
for e in es:
 a=date.fromisoformat(e['start']);b=date.fromisoformat(e['end'])+timedelta(days=1);assert b>a
 lines+=['BEGIN:VEVENT','UID:'+e['id']+'@school-calendar.local','DTSTAMP:'+now,'DTSTART;VALUE=DATE:'+a.strftime('%Y%m%d'),'DTEND;VALUE=DATE:'+b.strftime('%Y%m%d'),'SUMMARY:'+esc(e['title']),'CATEGORIES:'+esc(e['category']),'DESCRIPTION:非公式。学校の最新連絡を優先してください。','END:VEVENT']
lines+=['END:VCALENDAR'];(p/'calendar.ics').write_bytes(('\r\n'.join(map(fold,lines))+'\r\n').encode())
