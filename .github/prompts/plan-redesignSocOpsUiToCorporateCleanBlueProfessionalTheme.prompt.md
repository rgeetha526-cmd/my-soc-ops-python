## Plan: Redesign Soc Ops UI to Corporate Clean Blue Professional Theme

TL;DR: Transform the Soc Ops bingo app's UI from its current minimalist blue theme to a polished Corporate Clean Blue professional design, focusing on clean layouts, subtle gradients, professional typography, and enhanced visual hierarchy while maintaining HTMX functionality.

**Steps**
1. **Update CSS Foundation** — Redesign [app/static/css/app.css](app/static/css/app.css) with Corporate Clean Blue palette: primary #1e40af (deep blue), secondary #3b82f6 (bright blue), neutral grays (#f8fafc to #1e293b), clean whites. Add professional typography (Inter or system-ui), refined spacing, subtle shadows, and hover effects. Remove outdated utilities and add new ones for glass-like elements.
2. **Redesign Bingo Board Component** — Update [app/templates/components/bingo_board.html](app/templates/components/bingo_board.html) with new square styling: clean borders, subtle gradients on hover, professional marked states (deep blue instead of green), winning states with gold accents. Improve grid layout and responsiveness.
3. **Polish Bingo Modal** — Enhance [app/templates/components/bingo_modal.html](app/templates/components/bingo_modal.html) with professional overlay (semi-transparent dark blue), centered content, refined typography, and smooth entrance animation.
4. **Update Game Screen Layout** — Modify [app/templates/components/game_screen.html](app/templates/components/game_screen.html) for clean header design, professional button styling, and improved instructions layout.
5. **Refine Start Screen** — Update [app/templates/components/start_screen.html](app/templates/components/start_screen.html) with corporate branding, clean CTA button, and professional info card styling.
6. **Minor Base Template Tweaks** — Adjust [app/templates/base.html](app/templates/base.html) for theme-color meta tag and any necessary font imports.

**Relevant files**
- [app/static/css/app.css](app/static/css/app.css) — Complete overhaul of utility classes and color system
- [app/templates/components/bingo_board.html](app/templates/components/bingo_board.html) — Core visual component redesign
- [app/templates/components/bingo_modal.html](app/templates/components/bingo_modal.html) — Modal professional styling
- [app/templates/components/game_screen.html](app/templates/components/game_screen.html) — Layout and header updates
- [app/templates/components/start_screen.html](app/templates/components/start_screen.html) — Branding and CTA polish
- [app/templates/base.html](app/templates/base.html) — Minor meta and font adjustments

**Verification**
1. **Visual Inspection** — Start the app (`uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`) and manually verify the new Corporate Clean Blue theme across start screen, game board, and modal.
2. **Responsiveness Test** — Check layout on mobile, tablet, and desktop viewports to ensure clean scaling.
3. **Functionality Check** — Play a full game to confirm HTMX interactions, marking squares, win detection, and modal display work correctly.
4. **Accessibility Audit** — Verify sufficient color contrast, keyboard navigation, and screen reader compatibility.

**Decisions**
- **Theme Selection**: Corporate Clean Blue — Emphasizes cleanliness, professionalism, and subtle blue accents over flashy gradients or metallic effects.
- **Color Palette**: Primary #1e40af, Secondary #3b82f6, Success (marked) #1e40af with lighter variants, Winning gold #f59e0b, Neutrals grays and whites.
- **Typography**: System-ui stack with improved font weights and sizes for hierarchy.
- **Scope Boundaries**: Focus on visual redesign; no changes to game logic, backend, or core HTMX functionality. Maintain mobile-first responsive design.
- **Excluded**: Gradient Glass UI and Metallic Chrome elements to keep it truly "clean" and corporate.

**Further Considerations**
1. **Font Choice**: Stick with system fonts for broad compatibility, or add Inter if needed for more polish?
2. **Dark Mode**: Implement optional dark mode variant with dark blues and grays?
3. **Animation Polish**: Enhance transitions beyond current 150ms for more professional feel?
