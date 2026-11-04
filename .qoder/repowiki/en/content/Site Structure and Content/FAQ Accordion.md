# FAQ Accordion

<cite>
**Referenced Files in This Document**   
- [index.html](file://index.html)
- [en/index.html](file://en/index.html)
- [README.md](file://README.md)
</cite>

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Core Components](#core-components)
4. [Architecture Overview](#architecture-overview)
5. [Detailed Component Analysis](#detailed-component-analysis)
6. [Dependency Analysis](#dependency-analysis)
7. [Performance Considerations](#performance-considerations)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Conclusion](#conclusion)

## Introduction
This document explains the FAQ accordion built with native HTML `<details>` elements. It covers semantic markup, accessibility behavior, styling, keyboard navigation, mobile responsiveness, content organization, and guidance for adding new items and customizing appearance while keeping screen readers and keyboard-only users in mind.

The FAQ section is a self-contained part of a single-page website template that includes Italian and English versions. The accordion itself does not use JavaScript; its expand/collapse behavior comes from the browser’s native implementation of `<details>`.

## Project Structure
The FAQ lives inside the main page body as a dedicated section:
- Section element with `id="faq"` and `aria-labelledby` pointing to the visible heading.
- A list container with class `faq__list`.
- One `<details class="faq__item">` per question.
- Each item contains a `<summary class="m-text-7">` for the question and a paragraph `<p class="m-text faq__answer">` for the answer.

```mermaid
graph TB
Page["Page Body"] --> Section["Section #faq"]
Section --> Title["Heading #faq-title"]
Section --> List["Div .faq__list"]
List --> Item1["Details .faq__item"]
Item1 --> Summary1["Summary .m-text-7"]
Item1 --> Answer1["Paragraph .faq__answer"]
List --> Item2["Details .faq__item"]
Item2 --> Summary2["Summary .m-text-7"]
Item2 --> Answer2["Paragraph .faq__answer"]
```

**Diagram sources**
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:860-870](file://en/index.html#L860-L870)

**Section sources**
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:860-870](file://en/index.html#L860-L870)
- [README.md:26-28](file://README.md#L26-L28)

## Core Components
- Semantic container: `<section id="faq" aria-labelledby="faq-title">` groups the FAQ and links it to its heading.
- Question/answer pair: `<details>` provides the collapsible panel; `<summary>` is the clickable trigger; the answer is plain text inside the details element.
- Visual marker: an empty `<span class="faq__mark" aria-hidden="true">` next to each summary is styled to show a state change when the panel opens.
- Styling scope: CSS under `section:faq` targets `#faq`, `.faq__item`, `summary`, `.faq__mark`, and `.faq__answer`.

Key responsibilities:
- `<details>` manages open/closed state.
- `<summary>` is the accessible button-like control.
- CSS hides the default marker and adds a custom animated indicator.
- No JavaScript is required for basic functionality.

**Section sources**
- [index.html:860-870](file://index.html#L860-L870)
- [index.html:500-515](file://index.html#L500-L515)
- [en/index.html:860-870](file://en/index.html#L860-L870)
- [en/index.html:500-515](file://en/index.html#L500-L515)

## Architecture Overview
The FAQ accordion is a pure HTML/CSS component. Its behavior is driven by the browser’s native `<details>` API, while CSS handles layout, typography, borders, hover states, and the visual marker transition.

```mermaid
flowchart TD
User["User Interaction"] --> Keyboard["Keyboard or Mouse"]
Keyboard --> Summary["Summary Element"]
Summary --> Details["Native <details> State Change"]
Details --> OpenState{"Is Panel Open?"}
OpenState --> |Yes| ShowAnswer["Show Answer Content"]
OpenState --> |No| HideAnswer["Hide Answer Content"]
ShowAnswer --> Marker["CSS Updates .faq__mark"]
HideAnswer --> Marker
Marker --> ScreenReader["Screen Reader Announces State"]
```

[No diagram sources needed since this diagram shows conceptual workflow, not actual code structure]

## Detailed Component Analysis

### Semantic Markup Structure
- Section wrapper:
  - `id="faq"` identifies the section for navigation and animations.
  - `aria-labelledby="faq-title"` associates the section with its heading.
- Heading:
  - `id="faq-title"` is the label referenced by `aria-labelledby`.
- List container:
  - `class="faq__list"` groups items but is not a list element because each item is a `<details>` panel rather than a simple list item.
- Each item:
  - `<details class="faq__item">` represents one question/answer pair.
  - `<summary class="m-text-7">` is the interactive trigger.
  - `<p class="m-text faq__answer">` holds the answer text.

Accessibility highlights:
- `<summary>` is focusable and acts like a button.
- The decorative marker uses `aria-hidden="true"` so assistive technologies ignore it.
- The section heading provides context for screen readers.

**Section sources**
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:860-870](file://en/index.html#L860-L870)

### Expand and Collapse Behavior
The accordion expands and collapses through the native `<details>` mechanism:
- Clicking or pressing Enter/Space on `<summary>` toggles the `open` attribute.
- When `open` is present, the browser reveals the content after `<summary>`.
- The CSS selector `details[open] .faq__mark::after` scales the marker to indicate the open state.

```mermaid
sequenceDiagram
participant U as "User"
participant S as "Summary"
participant D as "Details"
participant C as "CSS"
U->>S : "Click or press Enter/Space"
S->>D : "Toggle open state"
D-->>C : "Attribute changes to open"
C-->>U : "Reveal answer and update marker"
```

**Diagram sources**
- [index.html:500-515](file://index.html#L500-L515)
- [index.html:860-870](file://index.html#L860-L870)

**Section sources**
- [index.html:500-515](file://index.html#L500-L515)
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:500-515](file://en/index.html#L500-L515)
- [en/index.html:860-870](file://en/index.html#L860-L870)

### Accessibility Features
- Keyboard support:
  - Tab moves focus between summaries.
  - Enter or Space toggles the panel.
  - Arrow keys are not automatically managed by `<details>`; if you add internal focusable controls inside answers, ensure they remain reachable via Tab.
- Screen reader support:
  - Summaries are announced as collapsible controls.
  - The open/closed state is exposed through the native `<details>` semantics.
  - Decorative markers should keep `aria-hidden="true"`.
- Focus visibility:
  - Global `:focus-visible` styles provide a visible outline for keyboard users.
- Landmarks and headings:
  - The section heading provides a clear landmark for scanning FAQs.

Recommendations for compliance:
- Keep questions concise and meaningful in `<summary>`.
- Avoid placing interactive controls directly inside `<summary>` unless necessary.
- If answers contain links or buttons, test them with keyboard-only navigation and screen readers.
- Preserve the existing `aria-hidden="true"` on decorative markers.

**Section sources**
- [index.html:145-163](file://index.html#L145-L163)
- [index.html:500-515](file://index.html#L500-L515)
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:145-163](file://en/index.html#L145-L163)
- [en/index.html:500-515](file://en/index.html#L500-L515)
- [en/index.html:860-870](file://en/index.html#L860-L870)

### Styling Approach
The FAQ styling is scoped under the `section:faq` layer:
- Container:
  - Uses grid layout with responsive columns at larger breakpoints.
  - Adds top border and padding to separate it from other sections.
- Items:
  - Borders separate each question.
  - The first item gets a top border for visual symmetry.
- Summary:
  - Flex layout aligns the question text and marker.
  - Removes the default marker and sets pointer cursor.
- Marker:
  - A bordered square with a colored inner dot.
  - Scales up when the panel is open.
  - Hover effects enhance interactivity cues.
- Answer:
  - Constrained max width and bottom padding for readability.

Responsive behavior:
- On screens wider than 900px, the FAQ switches to a two-column grid layout.
- On smaller screens, it stacks vertically.

```mermaid
flowchart TD
Start["Apply section:faq styles"] --> Layout["Grid layout for #faq"]
Layout --> Items["Style .faq__item borders"]
Items --> Summary["Style summary layout and remove default marker"]
Summary --> Marker["Style .faq__mark and open-state transform"]
Marker --> Answer["Style .faq__answer spacing and color"]
Answer --> Responsive["@media min-width: 900px two-column layout"]
```

**Diagram sources**
- [index.html:500-515](file://index.html#L500-L515)
- [en/index.html:500-515](file://en/index.html#L500-L515)

**Section sources**
- [index.html:500-515](file://index.html#L500-L515)
- [en/index.html:500-515](file://en/index.html#L500-L515)

### Mobile Responsiveness
- The FAQ section uses CSS Grid with a responsive breakpoint at 900px.
- Below 900px, the FAQ stacks into a single column.
- Above 900px, it splits into two columns with a gap.
- Typography and spacing scale using CSS variables and clamp-based sizing elsewhere in the design system.

Practical implications:
- On narrow screens, each question takes full width.
- Answers wrap naturally within the constrained max width.
- Touch targets are adequate because summaries have sufficient padding.

**Section sources**
- [index.html:500-515](file://index.html#L500-L515)
- [en/index.html:500-515](file://en/index.html#L500-L515)

### Content Organization Strategy
Each FAQ item follows a consistent pattern:
- One `<details class="faq__item">` per question.
- A short, scannable question in `<summary>`.
- A focused answer in a paragraph with class `faq__answer`.
- A decorative marker span with `aria-hidden="true"`.

Content best practices:
- Keep questions specific and user-focused.
- Keep answers concise and actionable.
- Use paragraphs for longer answers instead of dense blocks.
- Avoid embedding complex widgets inside answers unless necessary.

**Section sources**
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:860-870](file://en/index.html#L860-L870)

### Adding a New FAQ Item
To add another question:
1. Locate the `faq__list` container inside the `#faq` section.
2. Add a new `<details class="faq__item">`.
3. Inside it, add a `<summary class="m-text-7">` with the question text.
4. Include the marker span `<span class="faq__mark" aria-hidden="true"></span>` inside the summary.
5. Add a `<p class="m-text faq__answer">` with the answer.
6. Repeat the same change in both language files (`index.html` and `en/index.html`) to keep translations aligned.

Example structure (described without code):
- Create a new details item.
- Put the question in the summary.
- Put the answer in a paragraph after the summary.
- Keep the marker span for visual consistency.

**Section sources**
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:860-870](file://en/index.html#L860-L870)

### Customizing Appearance
You can customize the accordion by editing the `section:faq` styles:
- Colors:
  - Update colors through CSS variables defined in the tokens layer.
- Borders:
  - Modify `.faq__item` borders to change separators.
- Marker:
  - Adjust `.faq__mark` size, border, and background.
  - Change the open-state transform on `details[open] .faq__mark::after`.
- Spacing:
  - Adjust summary padding and answer padding.
- Layout:
  - Change the two-column breakpoint or column ratios in the media query.

Guidelines:
- Prefer modifying CSS variables where possible.
- Keep the marker visually distinct in both closed and open states.
- Maintain sufficient contrast for text and interactive elements.
- Test hover and focus states across devices.

**Section sources**
- [index.html:117-138](file://index.html#L117-L138)
- [index.html:500-515](file://index.html#L500-L515)
- [en/index.html:117-138](file://en/index.html#L117-L138)
- [en/index.html:500-515](file://en/index.html#L500-L515)

### Ensuring Accessibility Compliance
Checklist:
- Every `<summary>` has clear, descriptive text.
- Decorative markers use `aria-hidden="true"`.
- Headings form a logical hierarchy; the FAQ section heading introduces the list.
- Keyboard navigation works:
  - Tab reaches each summary.
  - Enter or Space toggles panels.
  - Any interactive controls inside answers are reachable via Tab.
- Screen readers announce:
  - Collapsible group context.
  - Open/closed state changes.
- Focus outlines remain visible.
- Color changes alone do not convey state; combine color with shape or position.

If you extend the FAQ with additional controls:
- Give each control a visible label or associate labels properly.
- Ensure focus order matches visual order.
- Avoid relying solely on mouse hover for critical information.

**Section sources**
- [index.html:145-163](file://index.html#L145-L163)
- [index.html:500-515](file://index.html#L500-L515)
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:145-163](file://en/index.html#L145-L163)
- [en/index.html:500-515](file://en/index.html#L500-L515)
- [en/index.html:860-870](file://en/index.html#L860-L870)

## Dependency Analysis
The FAQ accordion has minimal dependencies:
- HTML semantics: `<section>`, `<h2>`, `<details>`, `<summary>`, `<p>`.
- CSS layers: tokens, base, atoms, sections.
- No JavaScript is required for core accordion behavior.

External scripts such as GSAP and Lenis exist in the page but do not control the FAQ toggle. They manage smooth scrolling and other scene animations.

```mermaid
graph LR
HTML["HTML Semantics"] --> Details["<details> Toggle"]
CSS["CSS Layers"] --> Styles["FAQ Styles"]
Styles --> Visual["Marker and Layout"]
JS["GSAP/Lenis Scripts"] -.-> NotUsed["Not used for FAQ toggle"]
```

**Diagram sources**
- [index.html:565-575](file://index.html#L565-L575)
- [index.html:939-945](file://index.html#L939-L945)
- [index.html:500-515](file://index.html#L500-L515)
- [index.html:860-870](file://index.html#L860-L870)

**Section sources**
- [index.html:565-575](file://index.html#L565-L575)
- [index.html:939-945](file://index.html#L939-L945)
- [index.html:500-515](file://index.html#L500-L515)
- [index.html:860-870](file://index.html#L860-L870)

## Performance Considerations
- Native `<details>` is lightweight and requires no runtime logic for basic expansion.
- CSS transitions are GPU-friendly transforms on the marker.
- The FAQ does not introduce heavy assets or scripts.
- Keep answer content concise to avoid large DOM trees.
- If you add images or rich content inside answers, consider lazy loading and appropriate image formats.

[No sources needed since this section provides general guidance]

## Troubleshooting Guide
Common issues and fixes:
- Marker does not change when opening:
  - Verify the CSS selector for `details[open] .faq__mark::after`.
  - Ensure the marker span exists inside each summary.
- Default marker still appears:
  - Confirm the rule hiding the webkit details marker is applied.
- Keyboard toggle does not work:
  - Check that the element is a valid `<summary>` inside `<details>`.
  - Ensure no custom script prevents default behavior.
- Screen reader does not announce state:
  - Do not override `<details>` semantics with custom roles unless necessary.
  - Keep `aria-hidden="true"` only on decorative markers.
- Layout breaks on mobile:
  - Check the media query breakpoint and grid settings.
  - Validate that answers respect max width and padding.

**Section sources**
- [index.html:500-515](file://index.html#L500-L515)
- [index.html:860-870](file://index.html#L860-L870)
- [en/index.html:500-515](file://en/index.html#L500-L515)
- [en/index.html:860-870](file://en/index.html#L860-L870)

## Conclusion
The FAQ accordion is a simple, accessible, and maintainable component built entirely with native HTML and CSS. It relies on `<details>` for behavior, CSS for styling and animation, and semantic markup for accessibility. By following the documented structure, you can safely add new questions, customize the appearance, and ensure reliable keyboard and screen reader support across devices.

[No sources needed since this section summarizes without analyzing specific files]