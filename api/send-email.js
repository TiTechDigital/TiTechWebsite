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
    const { name, email, message, phone, company, service, language, attribution } = req.body;

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

    // Build simple, professional email body
    let emailBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
  
  <h2 style="color: #315cdb; border-bottom: 2px solid #315cdb; padding-bottom: 10px;">
    ${isItalian ? 'Nuova richiesta dal sito web' : 'New enquiry from website'}
  </h2>
  
  <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <tr>
      <td style="padding: 10px 0; font-weight: bold; width: 120px;">${isItalian ? 'Nome:' : 'Name:'}</td>
      <td style="padding: 10px 0;">${name}</td>
    </tr>
    <tr>
      <td style="padding: 10px 0; font-weight: bold;">Email:</td>
      <td style="padding: 10px 0;"><a href="mailto:${email}" style="color: #315cdb;">${email}</a></td>
    </tr>
    ${phone ? `
    <tr>
      <td style="padding: 10px 0; font-weight: bold;">${isItalian ? 'Telefono:' : 'Phone:'}</td>
      <td style="padding: 10px 0;"><a href="tel:${phone}" style="color: #315cdb;">${phone}</a></td>
    </tr>
    ` : ''}
    ${company ? `
    <tr>
      <td style="padding: 10px 0; font-weight: bold;">${isItalian ? 'Azienda:' : 'Company:'}</td>
      <td style="padding: 10px 0;">${company}</td>
    </tr>
    ` : ''}
    ${service ? `
    <tr>
      <td style="padding: 10px 0; font-weight: bold;">${isItalian ? 'Servizio:' : 'Service:'}</td>
      <td style="padding: 10px 0;">${service}</td>
    </tr>
    ` : ''}
  </table>
  
  <div style="margin: 20px 0;">
    <strong style="display: block; margin-bottom: 10px;">${isItalian ? 'Messaggio:' : 'Message:'}</strong>
    <div style="background: #f5f5f5; padding: 15px; border-left: 3px solid #315cdb;">
      ${message.replace(/\n/g, '<br>')}
    </div>
  </div>
  
  ${attribution && (attribution.source || attribution.medium) ? `
  <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 13px; color: #666;">
    <strong>${isItalian ? 'Origine:' : 'Attribution:'}</strong><br>
    ${attribution.source ? `${isItalian ? 'Fonte' : 'Source'}: ${attribution.source}<br>` : ''}
    ${attribution.medium ? `${isItalian ? 'Mezzo' : 'Medium'}: ${attribution.medium}<br>` : ''}
    ${attribution.campaign ? `${isItalian ? 'Campagna' : 'Campaign'}: ${attribution.campaign}<br>` : ''}
    ${attribution.landing ? `Landing: ${attribution.landing}<br>` : ''}
  </div>
  ` : ''}
  
  <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #999; text-align: center;">
    TiTech Digital · titechdigital.it · ${new Date().toLocaleString(isItalian ? 'it-IT' : 'en-GB')}
  </div>
  
</body>
</html>
    `.trim();

    // Send notification email to TiTech Digital
    // resend v3 does not throw on API errors: it returns { data, error }.
    // The field for the reply address in this SDK version is reply_to.
    const notification = await resend.emails.send({
      from: 'TiTech Digital Website <noreply@titechdigital.it>',
      to: 'info@titechdigital.it',
      reply_to: email,
      subject: `${subjectPrefix} - ${name}`,
      html: emailBody,
    });
    if (notification.error) {
      console.error('Resend notification error:', JSON.stringify(notification.error));
      return res.status(502).json({
        error: isItalian
          ? 'Errore durante l\'invio. Riprova o scrivi a info@titechdigital.it'
          : 'Error sending message. Please try again or email info@titechdigital.it'
      });
    }

    // Send simple thank you email to the customer
    const thankYouBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
  
  <h2 style="color: #315cdb;">
    ${isItalian ? `Ciao ${name.split(' ')[0]}` : `Hi ${name.split(' ')[0]}`}
  </h2>
  
  <p>${isItalian 
    ? 'Grazie per averci contattato. Abbiamo ricevuto la tua richiesta e ti risponderemo entro 24 ore.'
    : 'Thank you for contacting us. We have received your enquiry and will respond within 24 hours.'
  }</p>
  
  ${service ? `<p><strong>${isItalian ? 'Hai richiesto:' : 'You requested:'}</strong> ${service}</p>` : ''}
  
  <p>${isItalian
    ? 'Per qualsiasi informazione urgente, contattaci direttamente:'
    : 'For urgent matters, contact us directly:'
  }</p>
  
  <p>
    📧 <a href="mailto:info@titechdigital.it" style="color: #315cdb;">info@titechdigital.it</a><br>
    📞 <a href="tel:+393509205365" style="color: #315cdb;">+39 350 9205365</a><br>
    💬 <a href="https://wa.me/393509205365" style="color: #315cdb;">WhatsApp</a>
  </p>
  
  <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #999;">
    <strong>TiTech Digital</strong><br>
    ${isItalian ? 'Soluzioni digitali · Novara, Italia' : 'Digital solutions · Novara, Italy'}<br>
    <a href="https://www.titechdigital.it" style="color: #315cdb;">titechdigital.it</a>
  </div>
  
</body>
</html>
    `.trim();

    const thankYou = await resend.emails.send({
      from: 'TiTech Digital <info@titechdigital.it>',
      to: email,
      subject: isItalian 
        ? `Grazie ${name.split(' ')[0]}, abbiamo ricevuto la tua richiesta` 
        : `Thank you ${name.split(' ')[0]}, we received your enquiry`,
      html: thankYouBody,
    });

    // The enquiry reached us; a failed thank-you must not turn it into an error.
    if (thankYou.error) {
      console.error('Resend thank-you error:', JSON.stringify(thankYou.error));
    }

    // Return success
    return res.status(200).json({ 
      success: true, 
      messageId: notification.data && notification.data.id,
      thankYouId: thankYou.data && thankYou.data.id,
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
