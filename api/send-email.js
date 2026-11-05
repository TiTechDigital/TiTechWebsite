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

    // Send notification email to TiTech Digital
    const notificationEmail = await resend.emails.send({
      from: 'TiTech Digital Website <noreply@titechdigital.it>',
      to: 'info@titechdigital.it',
      replyTo: email,
      subject: `${subjectPrefix} - ${name}`,
      html: emailBody,
    });

    // Send thank you email to the customer
    const thankYouBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #101923; margin: 0; padding: 0; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { background: #315cdb; color: white; padding: 40px 30px; text-align: center; }
    .header h1 { margin: 0; font-size: 28px; font-weight: 800; }
    .content { background: #f7f8f6; padding: 40px 30px; }
    .greeting { font-size: 20px; font-weight: 700; color: #101923; margin-bottom: 20px; }
    .message { font-size: 16px; color: #25313c; margin-bottom: 20px; line-height: 1.6; }
    .info-box { background: white; padding: 25px; border-radius: 8px; border-left: 4px solid #315cdb; margin: 30px 0; }
    .info-label { font-weight: 600; color: #52606b; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
    .info-value { color: #101923; font-size: 16px; }
    .cta { text-align: center; margin: 30px 0; }
    .button { display: inline-block; background: #315cdb; color: white; padding: 14px 28px; text-decoration: none; border-radius: 4px; font-weight: 600; }
    .footer { padding: 30px; text-align: center; font-size: 13px; color: #52606b; border-top: 1px solid #e9edf0; }
    .footer a { color: #315cdb; text-decoration: none; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>${isItalian ? 'Grazie per averci contattato' : 'Thank you for contacting us'}</h1>
    </div>
    <div class="content">
      <p class="greeting">${isItalian ? `Ciao ${name.split(' ')[0]},` : `Hi ${name.split(' ')[0]},`}</p>
      
      <p class="message">
        ${isItalian 
          ? 'Abbiamo ricevuto la tua richiesta e ti risponderemo al più presto, solitamente entro 24 ore lavorative.'
          : 'We have received your enquiry and will respond as soon as possible, usually within 24 working hours.'}
      </p>
      
      <p class="message">
        ${isItalian
          ? 'Nel frattempo, ecco un riepilogo della tua richiesta:'
          : 'In the meantime, here is a summary of your enquiry:'}
      </p>
      
      <div class="info-box">
        ${service ? `
        <div style="margin-bottom: 15px;">
          <div class="info-label">${isItalian ? 'Servizio richiesto' : 'Service requested'}</div>
          <div class="info-value">${service}</div>
        </div>
        ` : ''}
        
        <div>
          <div class="info-label">${isItalian ? 'Tuo messaggio' : 'Your message'}</div>
          <div class="info-value">${message.substring(0, 150)}${message.length > 150 ? '...' : ''}</div>
        </div>
      </div>
      
      <p class="message">
        ${isItalian
          ? 'Se hai dimenticato qualcosa o vuoi aggiungere dettagli, rispondi direttamente a questa email.'
          : 'If you forgot something or want to add details, simply reply to this email.'}
      </p>
      
      <div class="cta">
        <a href="https://titechdigital.it/${isItalian ? 'lavori/' : 'en/work/'}" class="button">
          ${isItalian ? 'Guarda i nostri lavori' : 'See our work'}
        </a>
      </div>
      
      <p class="message" style="margin-top: 30px; font-size: 14px;">
        ${isItalian
          ? 'Puoi anche contattarci direttamente:'
          : 'You can also contact us directly:'}
      </p>
      
      <p class="message" style="font-size: 14px;">
        📧 <a href="mailto:info@titechdigital.it" style="color: #315cdb; text-decoration: none;">info@titechdigital.it</a><br>
        📞 <a href="tel:+393509205365" style="color: #315cdb; text-decoration: none;">+39 350 9205365</a><br>
        💬 <a href="https://wa.me/393509205365" style="color: #315cdb; text-decoration: none;">WhatsApp</a>
      </p>
    </div>
    
    <div class="footer">
      <p>
        <strong>TiTech Digital</strong><br>
        ${isItalian 
          ? 'Soluzioni digitali per imprese in Italia e mercati internazionali'
          : 'Digital solutions for businesses in Italy and international markets'}<br>
        Novara, Italia
      </p>
      <p style="margin-top: 20px;">
        <a href="https://titechdigital.it/${isItalian ? '' : 'en/'}">${isItalian ? 'Visita il sito' : 'Visit website'}</a> · 
        <a href="https://titechdigital.it/${isItalian ? 'privacy/' : 'en/privacy/'}">Privacy</a>
      </p>
    </div>
  </div>
</body>
</html>
    `.trim();

    const thankYouEmail = await resend.emails.send({
      from: 'TiTech Digital <info@titechdigital.it>',
      to: email,
      subject: isItalian 
        ? `Grazie ${name.split(' ')[0]}, abbiamo ricevuto la tua richiesta` 
        : `Thank you ${name.split(' ')[0]}, we received your enquiry`,
      html: thankYouBody,
    });

    // Return success
    return res.status(200).json({ 
      success: true, 
      messageId: notificationEmail.id,
      thankYouId: thankYouEmail.id,
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
