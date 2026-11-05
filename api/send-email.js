// Vercel Serverless Function for sending emails via Resend
// Environment variable needed: RESEND_API_KEY

import { Resend } from 'resend';

export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Check for API key
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    console.error('RESEND_API_KEY not configured');
    return res.status(500).json({ error: 'Email service not configured' });
  }

  try {
    const { name, email, message, phone, company, service, language } = req.body;

    // Validate required fields
    if (!name || !email || !message) {
      return res.status(400).json({ 
        error: 'Missing required fields: name, email, and message are required' 
      });
    }

    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({ error: 'Invalid email address' });
    }

    // Initialize Resend
    const resend = new Resend(apiKey);

    // Determine language for subject
    const isItalian = language === 'it';
    const subjectPrefix = isItalian ? 'Nuova richiesta dal sito' : 'New enquiry from website';

    // Build email body
    let emailBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #101923; }
    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
    .header { background: #315cdb; color: white; padding: 20px; border-radius: 8px 8px 0 0; }
    .content { background: #f7f8f6; padding: 30px; border-radius: 0 0 8px 8px; }
    .field { margin-bottom: 20px; }
    .label { font-weight: 600; color: #52606b; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; }
    .value { color: #101923; font-size: 16px; }
    .message-box { background: white; padding: 20px; border-radius: 4px; border-left: 4px solid #315cdb; margin-top: 10px; }
    .footer { margin-top: 30px; padding-top: 20px; border-top: 1px solid #e9edf0; font-size: 13px; color: #52606b; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1 style="margin: 0; font-size: 24px;">${subjectPrefix}</h1>
    </div>
    <div class="content">
      <div class="field">
        <div class="label">${isItalian ? 'Nome' : 'Name'}</div>
        <div class="value">${name}</div>
      </div>
      
      <div class="field">
        <div class="label">Email</div>
        <div class="value"><a href="mailto:${email}">${email}</a></div>
      </div>
      
      ${phone ? `
      <div class="field">
        <div class="label">${isItalian ? 'Telefono' : 'Phone'}</div>
        <div class="value"><a href="tel:${phone}">${phone}</a></div>
      </div>
      ` : ''}
      
      ${company ? `
      <div class="field">
        <div class="label">${isItalian ? 'Azienda' : 'Company'}</div>
        <div class="value">${company}</div>
      </div>
      ` : ''}
      
      ${service ? `
      <div class="field">
        <div class="label">${isItalian ? 'Servizio' : 'Service'}</div>
        <div class="value">${service}</div>
      </div>
      ` : ''}
      
      <div class="field">
        <div class="label">${isItalian ? 'Messaggio' : 'Message'}</div>
        <div class="message-box">${message.replace(/\n/g, '<br>')}</div>
      </div>
      
      <div class="footer">
        ${isItalian ? 'Ricevuto da' : 'Received from'}: titechdigital.it<br>
        ${isItalian ? 'Data' : 'Date'}: ${new Date().toLocaleString(isItalian ? 'it-IT' : 'en-GB', { 
          dateStyle: 'long', 
          timeStyle: 'short',
          timeZone: 'Europe/Rome'
        })}
      </div>
    </div>
  </div>
</body>
</html>
    `.trim();

    // Send email via Resend
    const data = await resend.emails.send({
      from: 'TiTech Digital Website <noreply@titechdigital.it>',
      to: 'info@titechdigital.it',
      replyTo: email,
      subject: `${subjectPrefix} - ${name}`,
      html: emailBody,
    });

    // Return success
    return res.status(200).json({ 
      success: true, 
      messageId: data.id,
      message: isItalian ? 'Richiesta inviata con successo' : 'Enquiry sent successfully'
    });

  } catch (error) {
    console.error('Error sending email:', error);
    
    // Return user-friendly error
    return res.status(500).json({ 
      error: req.body.language === 'it' 
        ? 'Errore durante l\'invio. Riprova o scrivi a info@titechdigital.it' 
        : 'Error sending message. Please try again or email info@titechdigital.it',
      details: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
}
