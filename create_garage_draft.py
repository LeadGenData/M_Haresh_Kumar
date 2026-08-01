import win32com.client
import os

def create_draft():
    try:
        outlook = win32com.client.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.To = 'HR@thegaragein.com'
        mail.Subject = 'Application: Head of Data Operations (15 Yrs Exp | Bengaluru) - M. Haresh Kumar'
        
        resume_path = r'C:\Users\hi\Desktop\31-Jul\M_Haresh_Kumar_Data_SQL_PowerBI_Resume.pdf'
        if os.path.exists(resume_path):
            mail.Attachments.Add(resume_path)
            print('Attached resume PDF successfully!')
            
        mail.HTMLBody = """
        <div style="font-family: Arial, sans-serif; font-size: 14px; color: #333; line-height: 1.6;">
          <p>Dear Hiring Team / Leadership Team,</p>
          
          <p>I am writing to express my strong interest in the <b>Head of Data Operations</b> position at <b>The Garage India</b> (Bengaluru).</p>
          
          <p>With <b>15.0 years of experience</b> leading cross-functional data operations, managing execution teams of 15+ members, and overseeing high-volume data intake pipelines (200K–300K+ monthly records), I specialize in building reliable data quality controls, SLA governance, and automated ETL workflows.</p>
          
          <h3 style="color: #1e3a8a;">Key Executive Alignments for The Garage India:</h3>
          <ul>
            <li><b>Data Operations & Team Leadership:</b> 15 years leading end-to-end data intake, validation rules, and quality control across enterprise datasets, managing team shift rosters and zero-breach SLA compliance.</li>
            <li><b>SQL & ETL Data Pipelines:</b> Deep expertise in MS SQL Server, complex query transformations, CTEs, Window Functions (<code>QUALIFY ROW_NUMBER()</code>), and pipeline optimization.</li>
            <li><b>Process & AI Automation:</b> Hands-on authoring of Python automation tools (<code>pandas</code>, <code>pywin32</code>, REST API loggers) and DataOps monitoring to reduce manual cycle times from 5 days down to 1 day.</li>
            <li><b>Data Governance & Quality Standards:</b> Strict enforcement of schema validation, deduplication rules, and metrics stewardship.</li>
          </ul>
          
          <p><b>Candidate Availability & Compensation:</b></p>
          <ul>
            <li><b>Location:</b> Bengaluru (In-Office / Hybrid)</li>
            <li><b>Notice Period:</b> Immediate Joiner (0 Days Notice)</li>
            <li><b>Live Web Portfolio:</b> <a href="https://leadgendata.github.io/M_Haresh_Kumar/">https://leadgendata.github.io/M_Haresh_Kumar/</a></li>
          </ul>
          
          <p>My clean master resume is attached for your review. I welcome the opportunity to discuss how my operational leadership can support The Garage India's population health data mission.</p>
          
          <p>Sincerely,<br>
          <b>M. Haresh Kumar</b><br>
          Senior Data Operations Lead & Analytics Specialist<br>
          📱 Phone: +91 9663683773<br>
          ✉️ Email: hareshmkumar9@gmail.com<br>
          🌐 Portfolio: <a href="https://leadgendata.github.io/M_Haresh_Kumar/">leadgendata.github.io/M_Haresh_Kumar/</a></p>
        </div>
        """
        
        mail.Save()
        print('Successfully created Outlook draft for HR@thegaragein.com!')
    except Exception as e:
        print('Error creating draft:', e)

if __name__ == '__main__':
    create_draft()
