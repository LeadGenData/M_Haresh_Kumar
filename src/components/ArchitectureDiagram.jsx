import React, { useState } from 'react';

/**
 * Reusable Architecture Diagram Component for React Portfolios.
 * Displays ChatGPT dark-theme architecture diagrams with fullscreen lightbox & zoom controls.
 */
export default function ArchitectureDiagram({ 
  src, 
  title = 'Architecture Workflow Diagram', 
  caption = 'Interactive technical system workflow diagram' 
}) {
  const [isFullscreen, setIsFullscreen] = useState(false);

  return (
    <div className="architecture-diagram-container" style={styles.wrapper}>
      {/* Header bar */}
      <div style={styles.header}>
        <div style={styles.headerTitleGroup}>
          <span style={styles.accentDot} />
          <h4 style={styles.title}>{title}</h4>
        </div>
        <button 
          onClick={() => setIsFullscreen(!isFullscreen)} 
          style={styles.fullscreenBtn}
          title="Toggle Fullscreen View"
        >
          {isFullscreen ? '✕ Close' : '⛶ Fullscreen'}
        </button>
      </div>

      {/* Main Diagram View */}
      <div style={isFullscreen ? styles.fullscreenOverlay : styles.diagramBox}>
        <img 
          src={src} 
          alt={title} 
          style={isFullscreen ? styles.fullscreenImg : styles.img} 
          loading="lazy"
        />
      </div>

      {/* Footer Caption */}
      {caption && <p style={styles.caption}>{caption}</p>}
    </div>
  );
}

const styles = {
  wrapper: {
    backgroundColor: '#0B1220',
    border: '1px solid #2A3B5C',
    borderRadius: '12px',
    padding: '16px',
    margin: '20px 0',
    boxShadow: '0 8px 24px rgba(0, 0, 0, 0.4)',
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '12px',
    paddingBottom: '8px',
    borderBottom: '1px solid #1E293B'
  },
  headerTitleGroup: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px'
  },
  accentDot: {
    width: '8px',
    height: '8px',
    borderRadius: '50%',
    backgroundColor: '#10A37F',
    boxShadow: '0 0 8px #10A37F'
  },
  title: {
    margin: 0,
    fontSize: '15px',
    fontWeight: 600,
    color: '#F8FAFC'
  },
  fullscreenBtn: {
    backgroundColor: '#131C2E',
    color: '#34D399',
    border: '1px solid #10A37F',
    borderRadius: '6px',
    padding: '4px 10px',
    fontSize: '12px',
    fontWeight: 600,
    cursor: 'pointer',
    transition: 'all 0.2s ease'
  },
  diagramBox: {
    width: '100%',
    overflow: 'hidden',
    borderRadius: '8px',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0B1220'
  },
  img: {
    width: '100%',
    height: 'auto',
    display: 'block',
    maxHeight: '800px',
    objectFit: 'contain'
  },
  caption: {
    margin: '10px 0 0 0',
    fontSize: '12px',
    color: '#94A3B8',
    textAlign: 'center'
  },
  fullscreenOverlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    width: '100vw',
    height: '100vh',
    backgroundColor: 'rgba(11, 18, 32, 0.95)',
    zIndex: 9999,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '40px'
  },
  fullscreenImg: {
    maxWidth: '95%',
    maxHeight: '95%',
    objectFit: 'contain',
    borderRadius: '12px',
    boxShadow: '0 12px 40px rgba(0,0,0,0.8)'
  }
};
