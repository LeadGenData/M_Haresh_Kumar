# SVG Architecture Diagram Design System Guide

A standardized vector design system for technical architecture diagrams optimized for GitHub READMEs, web documentation, and React portfolio applications. Inspired by ChatGPT's modern dark interface.

---

## 🎨 Visual Identity & Color Tokens

### Backgrounds & Surfaces
| Token Name | Hex Code | Purpose |
| --- | --- | --- |
| `bg-main` | `#0B1220` | Primary SVG background (Dark Obsidian) |
| `bg-card-dark` | `#131C2E` | Card base color |
| `bg-card-light` | `#1E293B` | Card header & nested container surface |
| `stroke-card` | `#2A3B5C` | Default card border stroke |
| `stroke-active` | `#10A37F` | Highlighted / active border stroke |

### Accent Palette (ChatGPT-Inspired)
| Accent Role | Color Hex | Sample Usage |
| --- | --- | --- |
| **Primary Accent (Teal)** | `#10A37F` | Key stage borders, callouts, active connectors |
| **Secondary Accent (Emerald)** | `#34D399` | Status text, checkmarks, badges |
| **Blue Accent** | `#38BDF8` | Ingestion layers, data clouds, connectors |
| **Amber Accent** | `#F59E0B` | Ingestion layers, Power BI components, highlights |
| **Purple Accent** | `#A855F7` | AI / Cortex LLM components |
| **Outcome Panel** | `#064E3B` | Bottom Business Outcomes panel background |

---

## 📐 Layout Grid & Typography

- **Container Canvas**: `viewBox="0 0 850 H"` (Height scales based on number of stages, typically 1100px-1120px).
- **Typography Stack**: `system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`
- **Text Hierarchies**:
  - Main Diagram Title: `24px / 700` (`#F8FAFC`)
  - Stage Title: `16px / 700` (`#F8FAFC`)
  - Subtitle / Description: `12px / 400` (`#CBD5E1` / `#94A3B8`)
  - Stage Badge Tag: `10px / 700` (`#10A37F` or stage accent)
  - Business Outcome KPI: `24px-26px / 800` (`#10B981` / `#38BDF8` / `#F59E0B`)

---

## 📦 Vector Technology Icons Catalog

All diagrams include pure vector inline `<g id="...">` definitions inside `<defs>` so there are no external dependencies or broken image URLs.

### Available Icons in Design System:
1. `icon-sql`: Relational database cylinder with query symbol (`#38BDF8`).
2. `icon-snowflake`: Multi-branch snowflake crystal (`#29B5E8`).
3. `icon-powerbi`: 3-tier vertical bar chart in yellow/amber (`#F59E0B`).
4. `icon-python`: Interlocking snakes in blue (`#3776AB`) & yellow (`#FFD43B`).
5. `icon-outlook`: Microsoft Outlook blue badge with envelope and green 'O' logo (`#0078D4` / `#107C41`).
6. `icon-excel`: Microsoft Excel green grid spreadsheet with 'X' logo (`#107C41`).
7. `icon-sheets`: Google Sheets green table grid (`#0F9D58`).
8. `icon-appsscript`: Google Apps Script bracket glyph (`#4285F4`).
9. `icon-html5`: HTML5 shield icon (`#E34F26`).
10. `icon-js`: JavaScript yellow square badge (`#F7DF1E`).
11. `icon-cortex`: Snowflake Cortex AI purple neural ring (`#A855F7`).

---

## 🔄 Vertical Workflow Connector Syntax

Each stage connects vertically to the next using linear gradient dashed/solid arrows and centered label pills:

```xml
<g transform="translate(425, 300)">
  <line x1="0" y1="0" x2="0" y2="45" stroke="url(#arrow-grad)" stroke-width="3" stroke-dasharray="4,4" marker-end="url(#arrowhead-teal)"/>
  <rect x="-85" y="12" width="170" height="20" rx="10" fill="#0B1220" stroke="#10A37F" stroke-opacity="0.6"/>
  <text x="0" y="26" font-size="9" font-weight="700" fill="#10A37F" text-anchor="middle">STAGE TRANSITION LABEL</text>
</g>
```

---

## 📊 Business Outcome Section (Bottom Panel)

Every diagram concludes with a standardized Business Outcome section containing KPI metric cards:

```xml
<g transform="translate(40, 895)">
  <rect x="0" y="0" width="770" height="180" rx="16" fill="url(#outcome-grad)" stroke="#10A37F" stroke-width="1.5" filter="url(#shadow-soft)"/>
  
  <g transform="translate(24, 20)">
    <circle cx="10" cy="10" r="10" fill="#10B981" fill-opacity="0.2"/>
    <path d="M 6 10 L 9 13 L 15 7" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round"/>
    <text x="30" y="15" font-size="14" font-weight="700" fill="#10B981" letter-spacing="1">BUSINESS OUTCOMES &amp; IMPACT</text>
  </g>

  <!-- 3 Metric Cards Grid -->
  <g transform="translate(24, 55)">
    <rect x="0" y="0" width="225" height="105" rx="10" fill="#0B1220" fill-opacity="0.75" stroke="#10A37F" stroke-opacity="0.3"/>
    <text x="16" y="34" font-size="24" font-weight="800" fill="#10B981">99.9%</text>
    <text x="16" y="54" font-size="12" font-weight="700" fill="#F8FAFC">Metric Title</text>
    <text x="16" y="72" font-size="10" fill="#94A3B8">Detailed ROI explanation text</text>
  </g>
</g>
```

---

## 🚀 Integration Options

### Option 1: GitHub README Embed
Use clean HTML or Markdown relative image links:
```markdown
![Snowflake Medallion Architecture](docs/assets/diagrams/snowflake_medallion_architecture.svg)
```

### Option 2: React Web Application Embed
Import the SVGs directly or use the `ArchitectureDiagram.jsx` wrapper component:
```jsx
import ArchitectureDiagram from './components/ArchitectureDiagram';

function PortfolioPage() {
  return (
    <ArchitectureDiagram 
      src="/assets/diagrams/snowflake_medallion_architecture.svg"
      title="Snowflake Medallion Architecture"
    />
  );
}
```
